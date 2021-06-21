// Animations
AOS.init({
  anchorPlacement: 'top-left',
  duration: 1000
});


const tabs = document.querySelectorAll('.pills-tab');
const tabsContainer = document.querySelector('#v-pills-tablist');
const tabsContent = document.querySelectorAll('.tab-pane');

const modal = document.querySelectorAll('modal')
const accordion = document.querySelector('#accordionEx')
const carouselItem = document.querySelector('#carousel-item')
const portfolioSection = document.querySelector('.portfolio-section')
const portfolioModal = document.querySelector('.modalPortfolio')
const showPortfolio = document.querySelector('#portfolio-link')
const portfolio = document.querySelector('.portfolio')

// portfolio modal //
showPortfolio.addEventListener('click', e=>{
    e.preventDefault()

    $.ajax({
    type: 'GET',
    url: '/portfolio/',
    success: function (response) {
        console.log(response.data)
    },
    error: function(error) {
        console.log(error)
    }

});
})

portfolio.addEventListener('hover', function(){
    portfolio.classList.add('border border-secondary')
})


// tab container //

// using event delagation requires selection of the parent element of the tabs
tabsContainer.addEventListener(
    'click',function (e) {
    //matching strategy using closest
    const clicked = e.target.closest('#v-pills-tab');
    console.log(clicked);

    if (!clicked) return;

    tabs.forEach(t => t.classList.remove('active'))
    tabsContent.forEach(c => c.classList.remove('show', 'active'))

    clicked.classList.add('active')

    document.querySelector(`#v-pills-${clicked.dataset.tab}`).classList.add('show', 'active');

});


portfolioSection.addEventListener('hover', function(e) {
    e.preventDefault();
    const portfolioLink = e.target.closest('#portfolio-link');
    console.log(portfolioLink)

    portfolioLink.style.bordercolor('#bdbbb5')
});

// accordion.addEventListener('click', function(e) {
//     const clicked = e.target.closest('.card-header');
//     console.log(clicked);
//
//     if (!clicked) return;
//
//     cardContent.forEach(c => c.classList.remove('show'))
//
//     // featureArrow.classList.replace('fa-angle-right', 'fa-angle-down')
//
//     document.querySelector(`#collapse-${clicked.dataset.tab}`).classList.add('show');
// });

