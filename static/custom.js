function search_jobs(){
  $.ajax({
    type: 'GET',
    url: "/scrap_times/",
    data: {search: $("#search_jo").val()},
    success: function (response) {
        $("#search_jo").value = response.search
    },
    error: function (response) {
    }
})
}