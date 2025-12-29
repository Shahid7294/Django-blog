// // let colors;
// document.querySelector('.like').addEventListener('click',function () {
//     console.log(this.style.color)
//     if (this.style.color==="red") {
//         this.style.color="gray"
//     } else {
//         this.style.color = 'red';
        
        
//     }
// })
// console.log(colors)

document.addEventListener('DOMContentLoaded', function () {
    const likeBtn = document.querySelector('.like');
    const userId = likeBtn.dataset.user;   // user id
    const key = `liked_user_${userId}`;

    // page load par check
    if (localStorage.getItem(key) === 'true') {
        likeBtn.style.color = 'red';
    }

    likeBtn.addEventListener('click', function () {
        if (this.style.color === 'red') {
            this.style.color = 'gray';
            localStorage.setItem(key, 'false');
        } else {
            this.style.color = 'red';
            localStorage.setItem(key, 'true');
        }
    });
});


document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.getElementById('commentToggle');
    const commentBox = document.getElementById('commentSection');

    toggleBtn.addEventListener('click', function () {
        if (commentBox.style.display === 'none') {
            commentBox.style.display = 'block';
        } else {
            commentBox.style.display = 'none';
        }
    });
});
