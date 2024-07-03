//Login
let login_modal = document.querySelector('#sign-in')
function show(){
    login_modal.classList.replace('hidden', 'flex')
}

function hide(){
    login_modal.classList.replace('flex', 'hidden')
}

const email = document.querySelector('#email')
const password = document.querySelector('#password')
let notif = document.querySelector('#notif')
function submit_form(_self, event){
    event.preventDefault()
    let request = new XMLHttpRequest()
    request.open('POST', '/api/auth/login/')
    request.setRequestHeader('Content-Type', 'application/json')

    request.send(JSON.stringify({
        'email': email.value,
        'password': password.value
        }))

    request.onloadend = async () => {
        let response = JSON.parse(request.responseText)
        if (response['message'] == 'success'){
            window.location.href = '/projects'
            self.submit()
        }else{
            notif.classList.replace('hidden', 'block')
        }
    }
}

//Sign Up
let sign_up = document.querySelector('#sign-up')
function show_signup(){
    sign_up.classList.replace('hidden', 'flex')
    hide()
}


function close_signup(){
    sign_up.classList.replace('flex', 'hidden')
}


let first_name = document.querySelector('#first-name')
let last_name = document.querySelector('#last-name')
let signUp_email = document.querySelector('#signup-email')
let signUp_password = document.querySelector('#signup-password')
let signUp_notif = document.querySelector('#signup-notif')
let confirm_password = document.querySelector('#confirm-password')

function sign_up_user(_self, event){
    event.preventDefault()

    let request = new XMLHttpRequest()
    let incorrect = false
    request.open('POST', '/api/auth/sign-up/')
    request.setRequestHeader('Content-type', 'application/json')

    if (signUp_password.value != confirm_password.value){
        signUp_notif.textContent = 'password and confirm password must match'
        incorrect = true
    }else{
        incorrect = false
    }

    if(!incorrect){
        request.send(JSON.stringify({
            'signup_email' : signUp_email.value,
            'first_name' : first_name.value,
            'last_name' : last_name.value,
            'signup_password' : signUp_password.value
        }))

        request.onloadend = () => {
            let response = JSON.parse(request.responseText)
            if (response['message'] == 'Success'){
                signUp_notif.textContent = ''
                show()
                close_signup()
                signUp_email.value = ''
                first_name.value = ''
                last_name.value = ''
                signUp_password.value = ''
                confirm_password.value = ''
            }else{
                signUp_notif.textContent = response['message']
            }
        }
    }
}