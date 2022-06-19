function deleteSportler(element) {

    if (window.confirm("Wollen Sie diesen Sportler wirklich löschen?")) {
        element.parentElement.submit(this);
    }
}

function deleteRadrennen(element) {

    if (window.confirm("Wollen Sie dieses Radrennen wirklich löschen?")) {
        element.parentElement.submit(this);
    }
}

function deleteSponsor(element) {

    if (window.confirm("Wollen Sie diesen Sponsor wirklich löschen?")) {
        element.parentElement.submit(this);
    }

}

