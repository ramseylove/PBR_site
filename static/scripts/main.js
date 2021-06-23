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

const alertBox = document.getElementById('alert-box')

const contactForm = document.querySelector('#contact-form')
const nameInput = document.querySelector('#id_name')
const fromEmailInput = document.querySelector('#id_from_email')
const messageInput = document.querySelector('#id_message')
const csrf = document.getElementsByName('csrfmiddlewaretoken')


// alert box
const handleAlert = (type, msg) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type}" role="alert">
          ${msg}
        </div>`
}

// tab container //

// using event delegation requires selection of the parent element of the tabs
tabsContainer.addEventListener(
    'click',function (e) {
    //matching strategy using closest
    const clicked = e.target.closest('.pills-tab');
    console.log(clicked);

    if (!clicked) return;

    tabs.forEach(t => t.classList.remove('active'))
    tabsContent.forEach(c => c.classList.remove('show', 'active'))

    clicked.classList.add('active')

    document.querySelector(`#v-pills-${clicked.dataset.tab}`).classList.add('show', 'active');

});

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

contactForm.addEventListener('submit', e=>{
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '',
        data: {
            'csrfmiddlewaretoken': csrf[0].value,
            'name': nameInput.value,
            'from_email': fromEmailInput.value,
            'message': messageInput.value,
        },
        success: function(response){
            console.log(response)
            contactForm.classList.add('not-visible')
            handleAlert('success', 'Email sent')
        },
        error: function(error){
            console.log(error)
            handleAlert('danger', 'Error sending email')
        }
    })
})


    // portfolio modal //
// showPortfolio.addEventListener('click', e=>{
//     e.preventDefault()
//
//     $.ajax({
//     type: 'GET',
//     url: '/portfolio/',
//     success: function (response) {
//         console.log(response.data)
//     },
//     error: function(error) {
//         console.log(error)
//     }
//
// });
// })
//
// portfolio.addEventListener('hover', function(){
//     portfolio.classList.add('border border-secondary')
// })


// portfolioSection.addEventListener('hover', function(e) {
//     e.preventDefault();
//     const portfolioLink = e.target.closest('#portfolio-link');
//     console.log(portfolioLink)
//
//     portfolioLink.style.bordercolor('#bdbbb5')
// });

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

