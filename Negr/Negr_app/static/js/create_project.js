function create_project(){
    $('#btn').click(function(){
        $.ajax('/create_project/', {
            'type': 'POST',
            'async': true,
            'datatype': 'json',
            'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id_name':$('#id_name').val()
                    },
                    'success': function(data){
                        document.getElementById('resp').innerHTML = data['resp'];
                        window.alert('Project has created')
                    }
            })
        })
    }


$(document).ready(function(){
    create_project();
})