$(document).on("submit", "form.generate__form", function (e) {
    e.preventDefault()
    file_name = $('#file_name').val()
    number = $('#numbers').val()
    var $this = $(this);
    var url = $this.attr("action");
    var method = $this.attr("method");
    var data = {
        file_name : file_name,
        number : number
    }
    console.log(url);
    jQuery.ajax({
        type: method,
        url:url,
        dataType: "json",
        data: data,
        success:function success(data) {
            console.log(data);
        }
    })
})
