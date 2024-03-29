var updateBtns = document.getElementsByClassName('update-cart')
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('product ID:', productId, 'Action: ', action)
        console.log("USER: ", user)
        if (user == "AnonymousUser") {
            console.log("Kullanıcı giriş yapmamış")
        } else {
            updateUserOrder(productId, action)
        }
    })

    function updateUserOrder(productId, action) {
        console.log("Giriş yapılı ve sepete ekleniyor")
        var url = '/user/update_item/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({'productId': productId, 'action': action})
        })

            .then((response) => {
                return response.json()
            })

            .then((data) => {
                var message = document.createElement("div")
                document.body.appendChild(message);
                message.id = "product-added-succesfuly"
                message.innerHTML = data;
                setTimeout(() => {
                    message.classList.add("closing-effect")
                }, 3000)
                setTimeout(function () {
                    message.remove()
                }, 4000);


            })
    }
}






