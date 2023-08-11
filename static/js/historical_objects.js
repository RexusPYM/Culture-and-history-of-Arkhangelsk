checkEmail = function(event, allow_sub= false) {
    event.preventDefault()
    const email = document.getElementById('email')
    $.ajax({
        type: "GET",
        url: 'http://127.0.0.1:8000/historical_object/existing_email',
        data: {email: email.value},
        dataType: "json",
        success: function (data) {
            if (!data["email"]) {
                document.getElementById('form-error').textContent = "Этот email уже подписан"
            } else {
                alert('Вы подписались на рассылку')
                $("#email_form").submit()
                //window.location.replace('http://127.0.0.1:8000/historical_object/subscribe_email')
            }
        }
    })
}
document.getElementById("email_form").addEventListener("submit",event => checkEmail(event))
