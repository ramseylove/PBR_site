'use strict';

const tabs = document.querySelectorAll('#v-pills-tab');
const tabsContainer = document.querySelector('.nav-pills-custom');
const tabsContent = document.querySelectorAll('.tab-pane');

// using event delagation requires selection of the parent element of the tabs
tabsContainer.addEventListener('click',function (e) {
    //matching strategy using closest
    const clicked = e.target.closest('#v-pills-tab');
    console.log(clicked);

    if (!clicked) return;
    tabs.forEach(t => t.classList.remove('active'))
    tabsContent.forEach(c => c.classList.remove('show active'))

    clicked.classList.add('active')

    document.querySelector(`#v-pills-${clicked.dataset.tab}`).classList.add('show active');

});