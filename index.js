function performMagic() {
    if (differences.length <= 0)
        return;
    const elementsToChange = document.getElementsByTagName('div');
    for (let i = 0; i < elementsToChange.length; i++) {
        element = elementsToChange.item(i);
        element.classList.add('magic-color');
    }
}

performMagic()