const Modal = function (options) {
    let { blurClose = true, closeCallback, timeout = 10000 } = options || {};
    if (closeCallback) this.closeCallback = closeCallback;
    this.element = document.createElement('div');
    const createModalHeader = () => {
        var modalHeader = document.createElement('div');
        modalHeader.classList.add('modal-header');

        this.modalClose = document.createElement('div');
        this.modalClose.classList.add('modal-close');
        this.modalClose.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><line x1="200" y1="56" x2="56" y2="200" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"/><line x1="200" y1="200" x2="56" y2="56" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="16"/></svg>';
        modalHeader.appendChild(this.modalClose);
        this.modalClose.addEventListener('click', async e => {
            await this.hidden(e);
        });
        return modalHeader;
    }
    this.timeout = timeout;
    this.element.classList.add('modal');

    const modalShadow = document.createElement('div');
    modalShadow.classList.add('modal-shadow');
    if (blurClose) {
        modalShadow.addEventListener('click', async e => {
            if (e.target == modalShadow) {
                await this.hidden(e);
            }
        });
    }

    this.modalBox = document.createElement('div');
    this.modalBox.appendChild(createModalHeader(this.element));

    this.modalContent = document.createElement('div');
    this.modalContent.classList.add('modal-content');

    this.modalBox.appendChild(this.modalContent);
    modalShadow.appendChild(this.modalBox);
    this.element.appendChild(modalShadow);
}

Modal.prototype.show = function () {
    this.element.classList.add('show');
    setTimeout(() => {
        this.element.classList.add('show-animation');
    }, 100);
}
Modal.prototype.hidden = async function (e) {
    try {
        if (this.hasOwnProperty('closeCallback')) await Promise.race([this.closeCallback(e), new Promise((resolve, reject) => setTimeout(() => resolve(), this.timeout))]);
    } catch (error) {
        console.error(error);
    }
    this.element.classList.remove('show-animation');
    setTimeout(() => this.element.classList.remove('show'), 100);
}
Modal.prototype.getElement = function () {
    return this.element;
}