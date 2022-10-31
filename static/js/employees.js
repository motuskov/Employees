function update_employee_list( department_pk, page ) {
    $( '.btn-department' ).removeClass( 'btn-primary' );
    $( '#btn-department-' + department_pk ).addClass( 'btn-primary' );
    var request_parameters = 'department=' + department_pk;
    if( page ) {
        request_parameters += '&page=' + page;
    }
    $( '#employee-list' ).load(
        'employee_list/',
        request_parameters,
        function( response, status, xhr ) {
            if( status == 'success' || status == 'notmodified' ) {
                $( '#employee-list-alert' ).hide();
                $( '#employee-list' ).show();
            } else {
                $( '#employee-list' ).hide();
                $( '#employee-list-alert' ).show();
            }
        }
    );
}
