function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // These HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function setupAjax() {
    fetch = (originalFetch => {
        return (...args) => {
            let [resource, config] = args;

            if (config && !csrfSafeMethod(config.method)) {
                config.headers = {
                    ...config.headers,
                    'X-CSRFToken' : csrftoken,
                };
            }

            return originalFetch(resource, config);
        }
    })(fetch);
}

document.addEventListener('DOMContentLoaded', function() {
    setupAjax();
});