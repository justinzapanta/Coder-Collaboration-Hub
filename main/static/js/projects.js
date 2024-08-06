// Drop Dot
function drop_dot(_this){
    let dot_menu = document.querySelector(`#post-card-men${_this.id}`)
    if (dot_menu.classList.contains('block')){
        dot_menu.classList.replace('block', 'hidden')
    }else{
        dot_menu.classList.replace('hidden', 'block')
    }
}

function drop_dot_close(_this){
    let dot_menu = document.querySelector(`#post-card-men${_this.id}`)
    dot_menu.classList.replace('block', 'hidden')
}

//Favorites
function add_favorite(this_){
    let request = new XMLHttpRequest()
    request.open('POST', '/api/projects/favorite/')
    request.setRequestHeader('Content-type', 'application/json')

    let id = this_.id
    let star = document.querySelector(`#${id}`)
    let project_id = this_.getAttribute('project-id')
    if(star.classList.contains('text-gray-500')){
        request.send(JSON.stringify({
            'project-id': project_id,
            'add' : true
            }))
        star.classList.replace('text-gray-500', 'text-yellow-400')
    }else{
        request.send(JSON.stringify({
            'project-id': project_id,
            'add' : false
            }))
        star.classList.replace('text-yellow-400', 'text-gray-500')
    }
    
}


//Post Project Model
let post_modal = document.querySelector('#post-modal')

function post_project(this_='for update', method='post'){
    const post_form = document.querySelector('#post-form-id')
    document.querySelector('#submit-notif').textContent = ''
    document.querySelector('#project-name').classList.replace('border-red-500', 'border-gray-300')
    github_link.classList.replace('border-red-500', 'border-gray-300')
    discord_link.classList.replace('border-red-500', 'border-gray-300')
    
    if (method == 'update'){
        document.querySelector('#post-button-text-id').textContent = 'Update project'
        document.querySelector('#post-project-title').textContent = 'Edit Project'

        post_modal.classList.replace('hidden', 'flex')

        const id = String(this_.id).replace('update-', '')
        const post_form_inputs = document.querySelectorAll('.post-project')
        const post_cart_info = document.querySelectorAll(`.post-card-${id}`)
        const card = document.querySelector(`#post-card-${id}`)

        post_form.setAttribute('form-method', 'update')
        post_form.setAttribute('project-id', id)
        
        //project name
        post_form_inputs[0].value = post_cart_info[2].textContent 
        // github link
        post_form_inputs[1].value = card.getAttribute('github-link')
        // discord link
        post_form_inputs[2].value = card.getAttribute('discord-link')
        //programming languages and frameword
        post_form_inputs[3].value = post_cart_info[4].textContent
        //description
        post_form_inputs[4].value = post_cart_info[3].textContent
        //upload image Label
        if (card.getAttribute('image')){
            document.querySelector('#upload-image-label').textContent = 'Update Image'
        }else{
            document.querySelector('#upload-image-label').textContent = 'Upload Project Image (optional)'
        }
        
    }else if(method == 'post'){
        document.querySelector('#post-button-text-id').textContent = 'Add new Project'
        post_form.setAttribute('form-method', 'post')
        document.querySelector('#upload-image-label').textContent = 'Upload Project Image (optional)'
        post_modal.classList.replace('hidden', 'flex')
    }
}

function close_post(){
    post_modal.classList.replace('flex', 'hidden')
    const post_form_inputs = document.querySelectorAll('.post-project')
    post_form_inputs.forEach((input) => {
        input.value = ''
    })
}


//submit post
let project_name = document.querySelector('#project-name')
let github_link = document.querySelector('#github-link')
let discord_link = document.querySelector('#discord-link')
let tools = document.querySelector('#tools')
let project_description = document.querySelector('#project-description')
let post_notif = document.querySelector('#submit-notif')
let upload_img = document.querySelector('#upload-img')

function submit_post(_this, event){
    event.preventDefault()
    const today = new Date();
    const yyyy = today.getFullYear()
    const mm = String(today.getMonth() + 1).padStart(2, '0')
    const dd = String(today.getDate()).padStart(2, '0')
    const formattedDate = `${yyyy}/${mm}/${dd}`
    const method = document.querySelector('#post-form-id').getAttribute('form-method')

    let request = new XMLHttpRequest()
    if (method == 'post'){
        request.open('POST', '/api/projects/post/')
    }else if (method == 'update'){
        request.open('POST', '/api/projects/update/')
    }
    request.setRequestHeader('X-Requested-With', 'XMLHttpRequest')

    if (String(github_link.value).includes('https://github.com/')){
        github_link.classList.replace('border-red-500', 'border-gray-300')
        if (String(discord_link.value).includes('https://discord.com/') || String(discord_link.value).includes('https://discord.gg/')){
            discord_link.classList.replace('border-red-500', 'border-gray-300')
            if (document.querySelector('#project-name').value.length <= 60){
                const form_data = new FormData()
                const data = {
                    'project-name' : project_name.value,
                    'github-link' : github_link.value,
                    'discord-link' : discord_link.value,
                    'tools' : tools.value,
                    'project-description' : project_description.value,
                    'current-date' : formattedDate,
                    }
    
                if (upload_img.files[0]){
                    data['image'] = upload_img.files[0]
                }
                if (method == 'update'){
                    data['project_id'] = _this.getAttribute('project-id')
                }
    
                for (key in data){
                    form_data.append(key, data[key])
                }
                
                request.send(form_data)
    
                request.onloadend = () => {
                    _this.submit()
                }
            }else{
                post_notif.textContent = 'ensure your project name is 60 characters or fewer'
                document.querySelector('#project-name').classList.replace('border-gray-300', 'border-red-500')
            }
        }else{
            post_notif.textContent = 'Incorrect Discord link'
            discord_link.classList.replace('border-gray-300', 'border-red-500')
        }
    }else{
        post_notif.textContent = 'Incorrect Github link'
        github_link.classList.replace('border-gray-300', 'border-red-500')
    }
}

function show_post_card_modal(_this){
    document.querySelector('#post-card-modal').classList.replace('hidden', 'flex')
    let post = document.querySelectorAll(`.${_this.id}`)
    document.querySelector('#post-card-modal-profile-image').src = post[0].src
    document.querySelector('#post-card-modal-user-name').textContent = post[1].textContent
    document.querySelector('#post-card-modal-project-name').textContent = post[2].textContent
    document.querySelector('#post-card-modal-description').textContent = String(post[3].textContent)
    document.querySelector('#github-link-button').href = _this.getAttribute('github-link')
    document.querySelector('#discord-link-button').href = _this.getAttribute('discord-link')

    document.querySelector('#post-card-modal-user-name').setAttribute('pid', _this.id)
    document.querySelector('#post-card-modal-profile-image').setAttribute('pid', _this.id)

    //check if the post have image
    if(_this.getAttribute('image')){
        const image_path = `${_this.getAttribute('image')}`
        document.querySelector('#default-carousel').classList.replace('hidden', 'block')
        document.querySelector('#post-card-model-img').style.backgroundImage = `url("${image_path}")`
    }else{
        document.querySelector('#default-carousel').classList.replace('block', 'hidden')
    }

}

function view_profile(this_){
    const project_id = this_.getAttribute('pid').replace('post-card-', '')
    const request = new XMLHttpRequest()
    request.open('POST', '/api/projects/view_owner/')
    request.setRequestHeader('Content-Type', 'application/json')
    request.send(JSON.stringify({project_id : project_id}))

    request.onloadend = () => {
        const result = JSON.parse(request.responseText)
        window.location.href = `/profile/${result['message']}`
    }
}

function close_post_modal(){
    document.querySelector('#post-card-modal').classList.replace('flex', 'hidden')
}

// dropdot menu

//Delete
function show_delete_modal(this_){
    document.querySelector('#delete-modal').classList.replace('hidden', 'flex')
    document.querySelector('#delete-modal-id').setAttribute('project-id', this_.id)
}

function hide_delete_modal(){
    document.querySelector('#delete-modal').classList.replace('flex', 'hidden')
}


function delete_post(this_){
    const request = new XMLHttpRequest()
    const form_data = new FormData()

    form_data.append('project_id', this_.getAttribute('project-id'))
    request.open('POST', '/api/projects/delete/')
    request.setRequestHeader('X-Requested-With', 'XMLHttpRequest')
    request.send(form_data)

    request.onloadend = () => {
        window.location.href = '/projects'
    }
}

