var updateBtns = document.getElementsByClassName('update-cart-amount')
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        var productId = this.dataset.product
        var action = this.dataset.action
        if (user == "AnonymousUser") {

        } else {
            updateUserOrder(productId, action)
        }
    })

    function updateUserOrder(productId, action) {
        var url = '/user/update-cart/'
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
                var cartItem=document.getElementById("product-id-"+productId)
                cartItem.remove()
                var message = document.createElement("div")
                document.body.appendChild(message);
                message.id = "favorite-product-delete"
                message.innerHTML = data;
                setTimeout(() => {
                    message.classList.add("closing-effect")
                }, 3000)
            })
    }
}


