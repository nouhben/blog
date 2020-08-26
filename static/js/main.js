const icons = document.getElementsByClassName('icon-img');
const counters = document.getElementsByClassName('counter');
for (let index = 0; index < icons.length; index++) {
    const element = icons[index];
    element.addEventListener('click', function () {
        if (element.classList.contains('activated')) {
            //substract the number of likes
            const num = Number(counters[index].innerHTML);
            counters[index].innerHTML = num - 1;
            //remove the class
            element.classList.remove('activated');
            //make ajax calls to update the DB
        } else {
            //increment the number of likes
            const num = Number(counters[index].innerHTML);
            counters[index].innerHTML = num + 1;
            //add the class to show the button as activated
            element.classList.add('activated');
            //make ajax calls to update the DB
        }
    });
}