var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var _clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);

const options = {
    clientSecret: _clientSecret
}

var elements = stripe.elements(options);
const paymentElement = elements.create('payment');
paymentElement.mount('#payment-element');


const form = document.getElementById('payment-form');

form.addEventListener('submit', async (event) => {
  event.preventDefault();

  const {error} = await stripe.confirmPayment({
    elements,
    confirmParams: {
        return_url: window.location.origin+'/checkout/success/',
    },
  });

  if (error) {
    const messageContainer = document.querySelector('#error-message');
    messageContainer.textContent = error.message;
  } else {

  }
});