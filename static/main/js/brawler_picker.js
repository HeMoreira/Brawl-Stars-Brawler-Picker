const brawler_card_list = document.querySelectorAll('.brawl-card');
console.log(brawler_card_list)

brawler_card_list.forEach(card => {
    const input = card.querySelector('.brawler-select');
    const image = card.querySelector('.brawler-image');
    const status = card.querySelector('.brawler-status');
    input.addEventListener('input', () => {
        changeBrawlerSelected(image, input);
    });
});

function changeBrawlerSelected(image, input) {
    console.log("aaaaaaaaaaa")
    const base_path = BRAWLER_ICONS_STATIC_URL
    var brawler_was_found = false
    namelist_of_brawlers_and_icons.forEach(brawler => {
        if(brawler.name === input.value) {
            image.src = base_path + brawler.icon
            brawler_was_found = true;
        }
    });
    if (brawler_was_found === false) {
        image.src = base_path + "glowbert_icon.png"
    }
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