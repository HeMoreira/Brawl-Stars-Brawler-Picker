const brawler_card_list = document.querySelectorAll('.brawl-card');
const UPDATE_CARD_API_URL = typeof BRAWLER_UPDATE_API_URL !== 'undefined' ? BRAWLER_UPDATE_API_URL : '/match/api/update-card/';

function getCsrfToken() {
    const name = 'csrftoken';
    const cookies = document.cookie ? document.cookie.split(';') : [];
    for (let cookie of cookies) {
        cookie = cookie.trim();
        if (cookie.startsWith(name + '=')) {
            return decodeURIComponent(cookie.substring(name.length + 1));
        }
    }
    return null;
}

function markCardUpdateRequired(card) {
    const statusElement = card.querySelector('.brawler-status');
    statusElement.textContent = 'UPDATE';
    statusElement.dataset.status = 'update';
    statusElement.style.backgroundColor = '#6f6f6f';
    statusElement.style.color = '#ffffff';
    statusElement.style.cursor = 'pointer';
    statusElement.style.boxShadow = 'none';
}

function changeStatusCard(card, updated_status_information) {
    const statusElement = card.querySelector('.brawler-status');
    statusElement.textContent = updated_status_information.status;
    statusElement.dataset.status = updated_status_information.status.toLowerCase();
    if (updated_status_information.quality_vs_enemies["0"] === undefined) {
        statusElement.setAttribute('data-tooltip', 
            `Rating: ${updated_status_information.rating}
            ---------------
            Fit-Against:
            - 1° Enemy: ${JSON.stringify(updated_status_information.quality_vs_enemies["3"])}
            - 2° Enemy: ${JSON.stringify(updated_status_information.quality_vs_enemies["4"])}
            - 3° Enemy: ${JSON.stringify(updated_status_information.quality_vs_enemies["5"])}`);
    } else {
        statusElement.setAttribute('data-tooltip', 
            `Rating: ${updated_status_information.rating}
            ---------------
            Fit-Against:
            - 1° Ally: ${JSON.stringify(updated_status_information.quality_vs_enemies["0"])}
            - 2° Ally: ${JSON.stringify(updated_status_information.quality_vs_enemies["1"])}
            - 3° Ally: ${JSON.stringify(updated_status_information.quality_vs_enemies["2"])}`);
    }
    applyStatusColor(statusElement);
}

function collectCardsState() {
    return Array.from(brawler_card_list).map((card, index) => {
        const input = card.querySelector('.brawler-select');
        const gadgetSelected = card.querySelector('.gadget-container .image-selected');
        const starpowerSelected = card.querySelector('.star-power-container .image-selected');

        return {
            index,
            name: input ? input.value.trim() : '',
            gadget_id: gadgetSelected ? parseInt(gadgetSelected.dataset.id || 0, 10) : 0,
            starpower_id: starpowerSelected ? parseInt(starpowerSelected.dataset.id || 0, 10) : 0,
        };
    });
}

async function sendUpdateRequest(clickedIndex) {
    const cards = collectCardsState();
    const payload = { cards, clicked_index: clickedIndex };
    const csrfToken = getCsrfToken();

    try {
        const response = await fetch(UPDATE_CARD_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken || '',
            },
            body: JSON.stringify(payload),
        });

        if (!response.ok) {
            console.error('Falha ao atualizar card:', response.statusText);
            return;
        }

        const data = await response.json();
        if (data.card_results) {
            data.card_results.forEach(result => {
                const card = brawler_card_list[result.index];
                if (card) {
                    changeStatusCard(card, result);
                }
            });
        }

        updateTeamSummary(data);
    } catch (error) {
        console.error('Erro na requisição de update card:', error);
    }
}

function updateTeamSummary(data) {
    const proficienciesOutput = document.getElementById('team-proficiencies-output');
    const qualityOutput = document.getElementById('quality-output');

    if (proficienciesOutput) {
        proficienciesOutput.textContent = JSON.stringify(data.team_proficiencies || {}, null, 2);
    }

    if (qualityOutput) {
        qualityOutput.textContent = JSON.stringify(data.relative_quality || [], null, 2);
    }
}

brawler_card_list.forEach((card, index) => {
    const input = card.querySelector('.brawler-select');
    const gadget_container = card.querySelector('.gadget-container');
    const star_power_container = card.querySelector('.star-power-container');
    const gadget_selector = gadget_container.querySelector('.gadget-select');
    const star_power_selector = star_power_container.querySelector('.star-power-select');
    const statusElement = card.querySelector('.brawler-status');

    input.addEventListener('input', () => {
        changeBrawlerSelected(card);
        markCardUpdateRequired(card);
    });

    gadget_container.addEventListener('click', () => {
        gadget_selector.classList.toggle('select-hide');
        star_power_selector.classList.add('select-hide');
    });

    star_power_container.addEventListener('click', () => {
        star_power_selector.classList.toggle('select-hide');
        gadget_selector.classList.add('select-hide');
    });

    statusElement.addEventListener('click', () => {
        if (statusElement.dataset.status === 'update') {
            sendUpdateRequest(index);
        }
    });
});

function changeBrawlerSelected(card) {
    const base_brawlers_path = BRAWLER_ICONS_STATIC_URL + 'brawlers/';
    const image = card.querySelector('.brawler-image');
    const input = card.querySelector('.brawler-select');
    const gadget_select = card.querySelector('.gadget-select');
    const star_power_select = card.querySelector('.star-power-select');
    const hipercharge_container = card.querySelector('.hipercharge-container');
    brawler = getTypedBrawler(input);

    if (brawler === null) {
        image.src = base_brawlers_path + 'glowbert_icon.png';
        resetBrawlerOptions(card);
        return;
    }

    image.src = base_brawlers_path + brawler.icon;
    changeBrawlerOptions(gadget_select, star_power_select, hipercharge_container);
    updateBrawlerSelectedComplements(card);
}

function getTypedBrawler(input) {
    var typed_brawler = null;
    main_brawler_info_list.forEach(brawler => {
        if (brawler.name === input.value) {
            typed_brawler = brawler;
        }
    });
    return typed_brawler;
}

function changeBrawlerOptions(gadget_select, star_power_select, hipercharge_container) {
    changeBrawlerOption(brawler.first_gadget, brawler.second_gadget, gadget_select);
    changeBrawlerOption(brawler.first_star_power, brawler.second_star_power, star_power_select);
    hipercharge_container.querySelector('.hipercharge-image').src = BRAWLER_ICONS_STATIC_URL + 'hipercharges/' + brawler.hipercharge;
}

function changeBrawlerOption(first_option_content, second_option_content, select) {
    let base_option_path = BRAWLER_ICONS_STATIC_URL;
    if (select.classList.contains('gadget-select')) {
        base_option_path = BRAWLER_ICONS_STATIC_URL + 'gadgets/';
    } else if (select.classList.contains('star-power-select')) {
        base_option_path = BRAWLER_ICONS_STATIC_URL + 'star-powers/';
    }

    select.innerHTML = '';
    const first_option = document.createElement('img');
    first_option.dataset.id = 1;
    first_option.src = base_option_path + first_option_content;
    const second_option = document.createElement('img');
    second_option.dataset.id = 2;
    second_option.src = base_option_path + second_option_content;
    select.appendChild(first_option);
    select.appendChild(second_option);
}

function resetBrawlerOptions(card) {
    const gadget_container = card.querySelector('.gadget-container');
    const star_power_container = card.querySelector('.star-power-container');
    const hipercharge_container = card.querySelector('.hipercharge-container');

    gadget_container.querySelector('.gadget-select').innerHTML = '';
    star_power_container.querySelector('.star-power-select').innerHTML = '';

    gadget_container.querySelector('.image-selected').src = BRAWLER_ICONS_STATIC_URL + 'gadgets/gadget_base.png';
    gadget_container.querySelector('.image-selected').dataset.id = '0';
    star_power_container.querySelector('.image-selected').src = BRAWLER_ICONS_STATIC_URL + 'star-powers/starpower_base.png';
    star_power_container.querySelector('.image-selected').dataset.id = '0';
    hipercharge_container.querySelector('.hipercharge-image').src = BRAWLER_ICONS_STATIC_URL + 'hipercharges/hipercharge_base.png';
}

function updateBrawlerSelectedComplements(card) {
    const gadget_container = card.querySelector('.gadget-container');
    const star_power_container = card.querySelector('.star-power-container');
    const gadget_selector = gadget_container.querySelector('.gadget-select');
    const star_power_selector = star_power_container.querySelector('.star-power-select');
    const gadget_selected = gadget_container.querySelector('.image-selected');
    const star_power_selected = star_power_container.querySelector('.image-selected');

    gadget_selector.querySelectorAll('img').forEach(option => {
        option.addEventListener('click', () => {
            updateBrawlerComplement(gadget_selected, option, card);
        });
    });
    star_power_selector.querySelectorAll('img').forEach(option => {
        option.addEventListener('click', () => {
            updateBrawlerComplement(star_power_selected, option, card);
        });
    });
}

function updateBrawlerComplement(selected_image, new_image, card) {
    selected_image.src = new_image.src;
    selected_image.dataset.id = new_image.dataset.id;
    markCardUpdateRequired(card);
}

function applyStatusColor(element) {
    const status = element.dataset['status'].trim().toLowerCase();

    if (status === 'awful') {
        element.style.backgroundColor = '#ff0000';
        element.style.color = 'var(--text-light)';
        element.style.boxShadow = '0 0 20px var(--text-dark)';
    } else if (status === 'bad') {
        element.style.backgroundColor = '#f1612d';
        element.style.color = 'var(--text-dark)';
        element.style.boxShadow = '0 0 10px var(--shadow)';
    } else if (status === 'ok') {
        element.style.backgroundColor = '#fea618';
        element.style.color = 'var(--text-dark)';
        element.style.boxShadow = '0 0 10px var(--shadow)';
    } else if (status === 'good') {
        element.style.backgroundColor = '#4fc737';
        element.style.color = 'var(--text-dark)';
        element.style.boxShadow = '0 0 10px var(--shadow)';
    } else if (status === 'great') {
        element.style.backgroundColor = '#128518';
        element.style.color = 'var(--text-light)';
        element.style.boxShadow = '0 0 20px var(--text-dark)';
    } else {
        element.style.backgroundColor = '#6f6f6f';
        element.style.color = 'var(--text-light)';
        element.style.boxShadow = '0 0 10px var(--shadow)';
    }
}

document.querySelectorAll('.brawler-status').forEach(element => {
    applyStatusColor(element);
});

brawler_card_list.forEach(card => {
    changeBrawlerSelected(card);
});