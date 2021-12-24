var updateBtns = document.getElementsByClassName('update-favorite')
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product ID:', productId, 'Action: ', action)
        console.log("USER: ", user)
        if (user == "AnonymousUser") {
            console.log("Kullanıcı giriş yapmamış")
        } else {
            updateUserFav(productId, action)
        }
    })

    function updateUserFav(productId, action) {
        var url = '/user/update-favorites/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken':csrftoken
            },
            body: JSON.stringify({'productId': productId, 'action': action})
        })

            .then((response) =>{
                return response.json()
            })

            .then((data) => {
                console.log('data:',data)
                location.reload()
            })
    }
}