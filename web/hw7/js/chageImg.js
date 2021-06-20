function changeImg() {
    var profile = document.getElementById('me')
    const i = Math.floor(Math.random()*3+1)
    profile.style.backgroundImage = 'url(images/user'+i+'.jpeg)'
}