function AddField(selector, _prefix_) {
    var addElement = $(selector).clone(true);
    var total_forms = $('#id_' + _prefix_ + '-TOTAL_FORMS').val();
    addElement.find(':input').each(function () {
        var name = $(this).attr('name').replace('-' + (total_forms - 1) + '-', '-' + total_forms + '-');
        var id = 'id_' + name;
        $(this).attr({
            'name': name,
            'id': id
        }).val("").removeAttr('checked');;
    });
    addElement.find('label').each(function () {
        $(this).text('field' + total_forms);
    });
    total_forms++;
    $('#id_' + _prefix_ + '-TOTAL_FORMS').val(total_forms);
    $(selector).after(addElement);
    return false;
}

$(document).on('click', '.add', function (e) {
    e.preventDefault();
    AddField('.form-row:last', 'form');
    return false;
});
