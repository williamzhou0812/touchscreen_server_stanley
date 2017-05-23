/**
 * Created by jonathanadhitama on 23/5/17.
 */
const SHOW_OTHER_FIELDS = "SPECIFY";
$(function() {
    $('.field-displayFrom').hide();
    $('.field-displayTo').hide();
    $('#id_display').change(function() {
        const value = $('#id_display').find(":selected").text();
        if (value === SHOW_OTHER_FIELDS) {
            //Show display from & display to fields
            $('.field-displayFrom').show();
            $('.field-displayTo').show();
        } else {
            //Hide display form & display to fields
            $('.field-displayFrom').hide();
            $('.field-displayTo').hide();
        }
    });
});