const brawler_card_list = document.querySelectorAll('.brawl-card');

async function sendUpdateRequest() {
    const cards = collectCardsState();
    const payload = { cards };
    const csrfToken = getCsrfToken();

    try {
        const response = await fetch(BRAWLER_UPDATE_API_URL, {
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
                    console.log(card, result);
                    changeStatusCard(card, result);
                }
            });
        }

        updateTeamSummary(data);
    } catch (error) {
        console.error('Erro na requisição de update card:', error);
    }
}

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

function changeStatusCard(card, updated_status_information) {
    const statusElement = card.querySelector('.brawler-status');
    statusElement.textContent = updated_status_information.status;
    statusElement.dataset.status = String(updated_status_information.status).toLowerCase();
    const idx = Number(updated_status_information.index);

    if (statusElement.dataset.status === 'invalid') {
        statusElement.setAttribute('data-tooltip', `Enter a valid brawler`);
        applyStatusColor(statusElement);
        return;
    }

    if ([0, 1, 2].includes(idx)) {
        statusElement.setAttribute('data-tooltip',
            `Rating: ${updated_status_information.rating}/100
            ---------------
            Fit-Against:
            1° Enemy: ${JSON.stringify(updated_status_information.quality_vs_enemies["3"]) }
            2° Enemy: ${JSON.stringify(updated_status_information.quality_vs_enemies["4"]) }
            3° Enemy: ${JSON.stringify(updated_status_information.quality_vs_enemies["5"]) }`);
    } else if ([3, 4, 5].includes(idx)) {
        statusElement.setAttribute('data-tooltip',
            `Rating: ${updated_status_information.rating}/100
            ---------------
            Fit-Against:
            1° Ally: ${JSON.stringify(updated_status_information.quality_vs_enemies["0"]) }
            2° Ally: ${JSON.stringify(updated_status_information.quality_vs_enemies["1"]) }
            3° Ally: ${JSON.stringify(updated_status_information.quality_vs_enemies["2"]) }`);
    } else {
        statusElement.setAttribute('data-tooltip', `Something went wrong...`);
    }
    applyStatusColor(statusElement);
}

function updateTeamSummary(data) {
    const yourTeamDetails = document.querySelector('.your-team-details .scroll-box');
    const enemyTeamDetails = document.querySelector('.enemy-team-details .scroll-box');
    
    if (yourTeamDetails) {
        updateTeamDetails(data.team_proficiencies["blue"], yourTeamDetails);
    }

    if (enemyTeamDetails) {
        updateTeamDetails(data.team_proficiencies["red"], enemyTeamDetails);
    }
}

function updateTeamDetails(team_data, team_details_element) {
    if (!team_data || typeof team_data !== 'object') {
        return;
    }

    team_details_element.innerHTML = '';

    const entries = Array.isArray(team_data)
        ? team_data
        : Object.entries(team_data);

    entries.forEach(entry => {
        let key;
        let value;

        if (Array.isArray(entry)) {
            [key, value] = entry;
        } else if (entry && typeof entry === 'object') {
            key = entry.key;
            value = entry.value;
        }
        if (key[0] != '_') {
            const attributeDiv = document.createElement('div');
            attributeDiv.textContent = `${key}: ${Math.trunc(value / 3)}`;
            team_details_element.appendChild(attributeDiv);
        }
    });
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
        updateStatusToUptateRequired(card);
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
            sendUpdateRequest();
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
    const hipercharge_image = hipercharge_container.querySelector('.hipercharge-image');
    const hipercharge_tooltip = hipercharge_container.querySelector('.hipercharge-tooltip-image');
    hipercharge_image.src = BRAWLER_ICONS_STATIC_URL + 'hipercharges/' + brawler.hipercharge[0];
    hipercharge_image.dataset.tooltip = brawler.hipercharge[1];
    if (hipercharge_tooltip) {
        hipercharge_tooltip.dataset.tooltip = brawler.hipercharge[1];
    }
}

function changeBrawlerOption(first_option_content, second_option_content, select) {
    let base_option_path = BRAWLER_ICONS_STATIC_URL;
    if (select.classList.contains('gadget-select')) {
        base_option_path = BRAWLER_ICONS_STATIC_URL + 'gadgets/';
    } else if (select.classList.contains('star-power-select')) {
        base_option_path = BRAWLER_ICONS_STATIC_URL + 'star-powers/';
    }

    select.innerHTML = '';
    const first_option_wrapper = document.createElement('div');
    first_option_wrapper.classList.add('tooltip-image');
    const first_option = document.createElement('img');
    first_option.dataset.id = 1;
    first_option.dataset.tooltip = first_option_content[1];
    first_option.src = base_option_path + first_option_content[0];
    first_option.classList.add('additional-power-option');
    first_option_wrapper.dataset.tooltip = first_option_content[1];
    first_option_wrapper.appendChild(first_option);

    const second_option_wrapper = document.createElement('div');
    second_option_wrapper.classList.add('tooltip-image');
    const second_option = document.createElement('img');
    second_option.dataset.id = 2;
    second_option.dataset.tooltip = second_option_content[1];
    second_option.src = base_option_path + second_option_content[0];
    second_option.classList.add('additional-power-option');
    second_option_wrapper.dataset.tooltip = second_option_content[1];
    second_option_wrapper.appendChild(second_option);

    select.appendChild(first_option_wrapper);
    select.appendChild(second_option_wrapper);
}

function resetBrawlerOptions(card) {
    const gadget_container = card.querySelector('.gadget-container');
    const star_power_container = card.querySelector('.star-power-container');
    const hipercharge_container = card.querySelector('.hipercharge-container');
    const gadget_tooltip = gadget_container.querySelector('.tooltip-image');
    const star_power_tooltip = star_power_container.querySelector('.tooltip-image');
    const hipercharge_tooltip = hipercharge_container.querySelector('.hipercharge-tooltip-image');

    gadget_container.querySelector('.gadget-select').innerHTML = '';
    star_power_container.querySelector('.star-power-select').innerHTML = '';

    const gadget_selected = gadget_container.querySelector('.image-selected');
    const star_power_selected = star_power_container.querySelector('.image-selected');
    const hipercharge_image = hipercharge_container.querySelector('.hipercharge-image');

    gadget_selected.src = BRAWLER_ICONS_STATIC_URL + 'gadgets/gadget_base.png';
    gadget_selected.dataset.id = '0';
    gadget_selected.dataset.tooltip = 'Select a Gadget';
    if (gadget_tooltip) {
        gadget_tooltip.dataset.tooltip = 'No Gadget';
    }

    star_power_selected.src = BRAWLER_ICONS_STATIC_URL + 'star-powers/starpower_base.png';
    star_power_selected.dataset.id = '0';
    star_power_selected.dataset.tooltip = 'Select a StarPower';
    if (star_power_tooltip) {
        star_power_tooltip.dataset.tooltip = 'No StarPower';
    }

    hipercharge_image.src = BRAWLER_ICONS_STATIC_URL + 'hipercharges/hipercharge_base.png';
    if (hipercharge_tooltip) {
        hipercharge_tooltip.dataset.tooltip = 'No Hipercharge';
    }
}

function updateBrawlerSelectedComplements(card) {
    const gadget_container = card.querySelector('.gadget-container');
    const star_power_container = card.querySelector('.star-power-container');
    const gadget_selector = gadget_container.querySelector('.gadget-select');
    const star_power_selector = star_power_container.querySelector('.star-power-select');
    const gadget_selected = gadget_container.querySelector('.image-selected');
    const star_power_selected = star_power_container.querySelector('.image-selected');
    const gadget_tooltip = gadget_container.querySelector('.tooltip-image');
    const star_power_tooltip = star_power_container.querySelector('.tooltip-image');

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

    if (gadget_tooltip) {
        gadget_tooltip.dataset.tooltip = gadget_selected.dataset.tooltip || gadget_selected.dataset.name || '';
    }
    if (star_power_tooltip) {
        star_power_tooltip.dataset.tooltip = star_power_selected.dataset.tooltip || star_power_selected.dataset.name || '';
    }
}

function updateBrawlerComplement(selected_image, new_image, card) {
    selected_image.src = new_image.src;
    selected_image.dataset.id = new_image.dataset.id;
    selected_image.dataset.tooltip = new_image.dataset.tooltip;
    const tooltip_wrapper = selected_image.closest('.tooltip-image');
    if (tooltip_wrapper) {
        tooltip_wrapper.dataset.tooltip = new_image.dataset.tooltip;
    }
    updateStatusToUptateRequired(card);
}

function updateStatusToUptateRequired(card) {
    const statusElement = card.querySelector('.brawler-status');
    statusElement.textContent = 'UPDATE';
    statusElement.dataset.status = 'update';
    statusElement.style.backgroundColor = '#878787';
    applyDefaultStatusDecoration(statusElement);
    statusElement.setAttribute('data-tooltip', 'Needs Update');
}


function applyDefaultStatusDecoration(element) {
    element.style.color = 'var(--text-dark)';
    element.style.boxShadow = '0 0 10px var(--shadow)';
}
function applyContrastStatusDecoration(element) {
    element.style.color = 'var(--text-light)';
    element.style.boxShadow = '0 0 20px var(--text-dark)';
}

document.querySelectorAll('.brawler-status').forEach(element => {
    applyStatusColor(element);
});

function applyStatusColor(element) {
    const status = element.dataset['status'].trim().toLowerCase();

    if (status === 'awful') {
        element.style.backgroundColor = '#ff0000';
        applyContrastStatusDecoration(element);
    } else if (status === 'bad') {
        element.style.backgroundColor = '#f1612d';
        applyDefaultStatusDecoration(element);
    } else if (status === 'hmm') {
        element.style.backgroundColor = '#f4822a';
        applyDefaultStatusDecoration(element);
    } else if (status === 'ok') {
        element.style.backgroundColor = '#fea618';
        applyDefaultStatusDecoration(element);
    } else if (status === 'oh') {
        element.style.backgroundColor = '#adc71a';
        applyDefaultStatusDecoration(element);
    } else if (status === 'good') {
        element.style.backgroundColor = '#4fc737';
        applyDefaultStatusDecoration(element);
    } else if (status === 'great') {
        element.style.backgroundColor = '#128518';
        applyContrastStatusDecoration(element);
    } else {
        element.style.backgroundColor = '#878787';
        applyDefaultStatusDecoration(element);
    }
}

brawler_card_list.forEach(card => {
    changeBrawlerSelected(card);
});