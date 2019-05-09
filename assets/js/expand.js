function expandPost(id) {
    var button = $('a[id=' + id + ']');
    if (button.text() == 'Read more') {
        button.text("Read less");
    } else {
        button.text("Read more");
    }

    $('div[id=' + id + ']').toggleClass("project-details", 1000);
};

function expandAbstract(id, shrinkText) {
    var button = $('a[id=' + id + ']');
    if (button.text() != 'Collapse') {
        button.text("Collapse");
    } else {
        button.text(shrinkText);
    }

    $('div[id=' + id + ']').toggleClass("abstract-details", 1000);
};
