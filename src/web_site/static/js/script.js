const multiplicationAlgorithms = ['karatsuba', 'schoolBook']
const impulsumUrl = '/v1/api/impulsum'


const reportResultCreate = (algorithmId, report) => {
    $(`#${algorithmId}_result`).html(
        `<ul class="list-group">
            <li class="list-group-item d-flex justify-content-between align-items-center">
                Multiplication Result
                <span class="badge bg-light rounded-pill text-black">${report.result.multiplication_result}</span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
                Complexity
                <span class="badge bg-light rounded-pill"><img src="${report.result.complexity_svg}" width="75"></span>
            </li>
            <li class="list-group-item d-flex justify-content-between align-items-center">
                Execution Time
                <span class="badge bg-success rounded-pill">${report.result.execution_time}</span>
            </li>
         </ul>`
    );
}

const quickBulkTestResultsReportCreate = (algorithms) => {
    let reportHtml = ''

    for (const algorithm of algorithms) {
        let resultsHtml = ''

        for (const result of algorithm.result) {
            resultsHtml += `<tr>
                            <th>
                                <span class="badge rounded-pill text-bg-secondary">${result.inputs}</span>
                            </th>
                            <th>${result.results.x}</th><th>${result.results.y}</th>
                            <td>${result.results.multiplication_result}</td>
                            <td><span class="badge rounded-pill text-bg-success">${result.results.execution_time}</span></td>
                        </tr>`

        }

        reportHtml += `<h5>${algorithm.name} Results</h5>
                        <div class="table-responsive">
                            <table class="table table-striped table-sm">
                                <thead>
                                <tr>
                                    <th scope="col">#</th>
                                    <th scope="col">X number</th>
                                    <th scope="col">Y number</th>
                                    <th scope="col">Multiplication Result</th>
                                    <th scope="col">Execution Time</th>
                                </tr>
                                </thead>
                                <tbody>
                                ${resultsHtml}
                                <tr>
                                    <th scope="row"></th>
                                    <td colspan="5"><b>Complexity :</b><img src="${algorithm.result[0].results.complexity_svg}" width="75"></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>`

    }
    $('#quickBulkTestResults').html(reportHtml)
}

const quickSingleTestFormHandling = (elementId) => {
    $(`#${elementId}`).on("submit", function (event) {
        event.preventDefault();

        let formValues = $(this).serializeArray();

        const postBody = {
            x_num: formValues[1].value,
            y_num: formValues[2].value,
            algorithm_id: formValues[0].value
        }
        $.ajax({
            url: `${impulsumUrl}/${0}/`,
            method: 'POST',
            data: JSON.stringify(postBody),
            contentType: 'application/json;charset=UTF-8',
            success: function (data) {
                console.log(data);
                reportResultCreate(postBody.algorithm_id, data);

            }
        });
        this.reset();
    });
}

const quickBulkTestFormHandling = (elementId) => {
    $(`#${elementId}`).on("submit", function (event) {
        event.preventDefault();

        let formValues = $(this).serializeArray();
        const postBody = [
            {input_1: {x: formValues[0].value, y: formValues[1].value}},
            {input_2: {x: formValues[2].value, y: formValues[3].value}},
            {input_3: {x: formValues[4].value, y: formValues[5].value}},
            {input_4: {x: formValues[6].value, y: formValues[7].value}},
        ]

        $.ajax({
            url: `${impulsumUrl}/${1}/`,
            method: 'POST',
            data: JSON.stringify(postBody),
            contentType: 'application/json;charset=UTF-8',
            success: function (data) {
                console.log(data.results.algorithms)
                quickBulkTestResultsReportCreate(data.results.algorithms);
            }
        });
        this.reset();
    });
}

const randomBulkInputNumbersGenerate = () => {
    $('#randomBulkInputNumber').on('click', function () {
        for (let i = 1; i < 5; i++) {
            $(`input[name=${i}_number_input_x]`).val(Math.floor(Math.random() * 999999999));
            $(`input[name=${i}_number_input_y]`).val(Math.floor(Math.random() * 999999999));
        }
    });
}

$(document).ready(function () {
    multiplicationAlgorithms.forEach(function (item) {
        quickSingleTestFormHandling(item);
    });
    quickBulkTestFormHandling('bulk_test_form');
    randomBulkInputNumbersGenerate();
})