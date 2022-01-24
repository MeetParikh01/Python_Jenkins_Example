//<script>
//var logout_form = $("#logout_form")
//var sign_out = $("#sign_out")
//
//
//logout_form.submit(function (e){
//    e.preventDefault();
//    alert("block stopped")
//});
//alert("Hello");

var sign_out = $("#sign_out, #refused_logout")


sign_out.click(function (element) {
    let csrftoken = $("[name=csrfmiddlewaretoken]").val();
    let url = $(this).data("url")
//    let loginUrl = $(this).data("login-url")
    let loginUrl = "/accounts/login/"
//    postData(url).then(d => console.log(d))
//    data = postData(url).then(function(response){
//        alert(response.json())
//    })


//    *************************************
    let response = fetch(
        url,
        {
            method: 'POST',
//            redirect: 'follow',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            }
        }
    ).then(res => res.json())
    response.then(function(data) {
        $(location).prop("href", data.url)
//    debugger;
//    alert(data.status)
    })
//    alert(data)
//    $(location).prop("href", loginUrl)
});
//</script>