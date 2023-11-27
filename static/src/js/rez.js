document.addEventListener('DOMContentLoaded', function () {
    const checkinDateInput = document.querySelector('[name="checkin_date"]');
    const checkoutDateInput = document.querySelector('[name="checkout_date"]');

    const today = new Date().toISOString().split('T')[0];

    checkinDateInput.setAttribute('min', today);

    checkinDateInput.addEventListener('change', function () {
        checkoutDateInput.setAttribute('min', this.value);
        checkoutDateInput.value = '';
    });
});
