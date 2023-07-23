$(function() {
    $('input[name="ui_type"]').on('click', function() {
        if ($(this).val() == 'Srna')  {
            $('#srna_textbox').show();


            $('#utr_textbox').hide();
            $("#id_ui_text_utr").val("");
       
            $('#cds_textbox').hide();
            $("#id_ui_text_cds").val("");

            $('#ancrna_textbox').hide();
            $("#id_ui_text_ancrna").val("");

         

            


        }
        else if ($(this).val() == 'Utr') {
            $('#srna_textbox').hide();
            $("#id_ui_text_srna").val("");

            $('#utr_textbox').show();

            $('#cds_textbox').hide();
            $("#id_ui_text_cds").val("");

            $('#ancrna_textbox').hide();
            $("#id_ui_text_ancrna").val("");

        }
        else if ($(this).val() == 'Cds') {
            $('#srna_textbox').hide();
            $("#id_ui_text_srna").val("");

            $('#utr_textbox').hide();
            $("#id_ui_text_utr").val("");

            $('#cds_textbox').show();

            $('#ancrna_textbox').hide();
            $("#id_ui_text_ancrna").val("");

        }
        else if ($(this).val() == 'Annotated_ncrna') {
            $('#srna_textbox').hide();
            $("#id_ui_text_srna").val("");

            $('#utr_textbox').hide();
            $("#id_ui_text_utr").val("");

            $('#cds_textbox').hide();
            $("#id_ui_text_cds").val("");

            $('#ancrna_textbox').show();
        }  
        else {
            $('#srna_textbox').hide();
            $("#id_ui_text_srna").val("");

            $('#utr_textbox').hide();
            $("#id_ui_text_utr").val("");

            $('#cds_textbox').hide();
            $("#id_ui_text_cds").val("");

            $('#ancrna_textbox').hide();
            $("#id_ui_text_ancrna").val("");

        }
    });
});

