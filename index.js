function performMagic() {
    console.log('entered perform Magic')
    if (!differences.includes('+')) {
        console.log('cant perform magic')
        return;
    }
    const elementsToChange = document.getElementsByTagName('div');
    for (let i = 0; i < elementsToChange.length; i++) {
        element = elementsToChange.item(i);
        element.classList.add('magic-color');
    }
    console.log('performedMagic');
}

performMagic()