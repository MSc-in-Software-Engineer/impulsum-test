const multiplicationAlgorithms = ['karatsuba', 'toomCook', 'schoolBook', 'strassen']
const impulsumUrl = '/v1/api/impulsum'

const formHandling = (elementId) => {
    $(`#${elementId}`).on("submit", function (event) {
        event.preventDefault();

        let formValues = $(this).serializeArray();

        const postBody = {
            x_num: formValues[0].value,
            y_num: formValues[1].value,
            algorithm_id: formValues[2].value
        }
        console.log(postBody)
        $.ajax({
            url: impulsumUrl,
            method: 'POST',
            data: JSON.stringify(postBody),
            contentType: 'application/json;charset=UTF-8',
            success: function (data) {
                console.log(data);
                $(`#${elementId}_result`).html(JSON.stringify(data));
            }
        });
        this.reset();
    });
}

$(document).ready(function () {
    multiplicationAlgorithms.forEach(function (item) {
        formHandling(item);
    });
})