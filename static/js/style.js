function linkButtons(id) {
    var name = id.slice(5);

    var url = window.location.href.split('/')

    while (name[0] == '^') {
        url.pop();
        name = name.slice(1);
    }

    urlString = url.join('/')
    console.log(urlString)

    window.location = urlString.concat(name);
}