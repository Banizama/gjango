function create_task(){
    $('#btn').click(function(){
        $.ajax($('#btn').data('url'), {
            'type': 'POST',
            'async': true,
            'datatype': 'json',
            'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id_name':$('#id_name').val(),
                    'id_status':$('#id_status').val(),
                    'id_deadline':$('#id_deadline').val(),
                    'id_priority':$('#id_priority').val()
                    },
                    'success': function(data){
                        document.getElementById('resp').innerHTML = data;
                        window.alert('Task has created')
                    }
            })
        })
    }

$(function(){
    $(document).click(function(event){
        var element = $(event.target)
        if (element.attr('class') == 'edit_task'){

            $.ajax(element.data('url'),{
            'type': 'POST',
            'async': true,
            'datatype': 'json',
            'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'id': element.attr('id')
                    },
                    'success': function(data){
                        document.getElementById('form'+element.attr('id')).innerHTML = data;
                    }
            })}
                console.log($('.form').length)
           })
    })



function edit_task(){
    $('#apply_changes').click(function(){
            $.ajax($('#apply_changes').data('url'),{
            'type': 'POST',
            'async': true,
            'datatype': 'json',
            'data': {
                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
                    'task': $('#apply_changes').data('id'),
                    'id_change_name':$('#text_id').val(),
                    'id_change_status':$('#status_id').val(),
                    'id_change_deadline':$('#deadline_id').val(),
                    'id_change_priority':$('#priority_id').val()
                    },
                    'success': function(data){
                        document.getElementById(`task_info${$('#apply_changes').data('id')}`).innerHTML = data;
//                        document.getElementById('form')).innerHTML = dta;

                    }

            })
    })
}


//function edit_task(){
//    $(document).click(function(event){
//        var element = $(event.target)
//        if (element.attr('class') == 'edit_task'),{
//            'type': 'POST',
//            'async': true,
//            'datatype': 'json',
//            'data': {
//                    'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
//                    'id_name':$('#id_name').val(),
//                    'id_status':$('#id_status').val(),
//                    'id_deadline':$('#id_deadline').val(),
//                    'id_priority':$('#id_priority').val()
//                    },
//                    'success': function(data){
//                        document.getElementById('task_info').innerHTML = data;
//                        window.alert('Task has been edited')
//                    }
//            })
//        })
//    }
//
//
//
//
//
//$(document).ready(function(){
//    create_task();
//})