$(document).ready(() => {
    const f = $('#login_form');
    f.find('button').click((ev) => {
        ev.preventDefault();
        const name = f.find('[name=username').val();
        alert(`Hello ${name}`);
    });
});
