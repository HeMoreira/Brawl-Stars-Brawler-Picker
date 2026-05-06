const brawler_card_list = document.querySelectorAll('.brawl-card');
console.log(brawler_card_list)

brawler_card_list.forEach(card => {
    const input = card.querySelector('.brawler-select');
    const gadget_container = card.querySelector('.gadget-container');
    const star_power_container = card.querySelector('.star-power-container');
    input.addEventListener('input', () => {
        changeBrawlerSelected(card);
    });
    gadget_container.addEventListener('click', () => {
        gadget_selector = gadget_container.querySelector('.gadget-select')
        gadget_selector.classList.toggle('select-hide');
        star_power_container.querySelector('.star-power-select').classList.add('select-hide');
    });
    star_power_container.addEventListener('click', () => {
        star_power_selector = star_power_container.querySelector('.star-power-select')
        star_power_selector.classList.toggle('select-hide');
        gadget_container.querySelector('.gadget-select').classList.add('select-hide');
    });
});

function changeBrawlerSelected(card) {
    const base_brawlers_path = BRAWLER_ICONS_STATIC_URL + 'brawlers/';
    const image = card.querySelector('.brawler-image');
    const input = card.querySelector('.brawler-select');
    const gadget_select = card.querySelector('.gadget-select');
    const star_power_select = card.querySelector('.star-power-select');
    brawler = getTypedBrawler(input);
    if (brawler === null) {
        image.src = base_brawlers_path + "glowbert_icon.png"
        resetBrawlerOptions(gadget_select, star_power_select);
        return;
    }

    image.src = base_brawlers_path + brawler.icon
    
    changeBrawlerOptions(gadget_select, star_power_select);
}

function getTypedBrawler(input) {
    var typed_brawler = null;
    main_brawler_info_list.forEach(brawler => {
        if(brawler.name === input.value) {
            typed_brawler = brawler;
        }
    });
    return typed_brawler;
}

function changeBrawlerOptions(gadget_select, star_power_select) {
    changeBrawlerOption(brawler.first_gadget, brawler.second_gadget, gadget_select);
    changeBrawlerOption(brawler.first_star_power, brawler.second_star_power, star_power_select);
}

function changeBrawlerOption(first_option_content, second_option_content, select) {
    base_option_path = BRAWLER_ICONS_STATIC_URL;
    if(select.classList.contains('gadget-select')) {
        base_option_path = BRAWLER_ICONS_STATIC_URL + 'gadgets/';
    } else if(select.classList.contains('star-power-select')) {
        base_option_path = BRAWLER_ICONS_STATIC_URL + 'star-powers/';
    }

    first_option = document.createElement('img');
    first_option.value = 1;
    first_option.src = base_option_path + first_option_content;
    second_option = document.createElement('img');
    second_option.value = 2;
    second_option.src = base_option_path + second_option_content;
    select.appendChild(first_option);
    select.appendChild(second_option);
}

function resetBrawlerOptions(gadget_select, star_power_select) {
    gadget_select.innerHTML = '';
    star_power_select.innerHTML = '';
}

function applyStatusColor(element) {
    const status = element.dataset['status'].trim().toLowerCase();
    
    if (status === 'awful') {
        element.style.backgroundColor = '#ff0000'
        element.style.boxShadow = '0 0 20px var(--text-dark)'
    } else if (status === 'bad') {
        element.style.backgroundColor = '#f1612d'
        element.style.color = 'var(--text-dark)'
    } else if (status === 'ok') {
        element.style.backgroundColor = '#fea618'
        element.style.color = 'var(--text-dark)'
    } else if (status === 'good') {
        element.style.backgroundColor = '#4fc737'
        element.style.color = 'var(--text-dark)'
    } else if (status === 'great') {
        element.style.backgroundColor = '#128518'
        element.style.boxShadow = '0 0 20px var(--text-dark)'
    } else {
        element.style.backgroundColor = '#828282'
        element.style.color = 'var(--text-dark)'
        element.textContent = 'undefined'
    }
}

document.querySelectorAll('.brawler-status').forEach(element => {
    applyStatusColor(element);
});