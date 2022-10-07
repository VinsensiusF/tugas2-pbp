const row = document.getElementById('row')

$(document).ready(() => {
  $.get('/todolist/show-json', (tasks) => {
    tasks.forEach((task) => {
      $('#row').append(`
        <div class="col mt-2 ml-2 mb-2 mr-2">
            <div class="card text-white bg-dark" style="width: 18rem;">
                <div class="container">
                    <div class="text-center bg-success">
                        <h7 class="tanggal">${task.fields.date}</h5>
                    </div>
                    <div class="card-body">
                        <h5 class="judul"><b>${task.fields.title}</b></h5>
                        <p class="description">${task.fields.description}</p>
                    </div>
                </div>
            </div>
        </div>
      `)
    })
  })
  $('#form').submit((e) => {
    e.preventDefault()
    $.ajax({
      url: '/todolist/ajax/submit',
      type: 'POST',
      dataType: 'json',
      data: $('#form').serialize(),
      success: (respond) => {
        console.log(respond)
        $('#modal-ajax').modal('hide')
        $('#row').append(`
          <div class="col mt-2 ml-2 mb-2 mr-2">
              <div class="card text-white bg-dark" style="width: 18rem;">
                  <div class="container">
                      <div class="text-center bg-success">
                          <h7 class="tanggal">${task.fields.date}</h5>
                      </div>
                      <div class="card-body">
                          <h5 class="judul"><b>${task.fields.title}</b></h5>
                          <p class="description">${task.fields.description}</p>
                      </div>
                  </div>
              </div>
          </div>
        `)
      },
      error: () => {
        alert("ERROR")
      }
    })
  })
  });
Footer
