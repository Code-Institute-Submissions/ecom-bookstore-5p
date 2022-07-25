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


  $.post('/checkout', postData).done
  const {error} = await stripe.confirmPayment({
    //`Elements` instance that was used to create the Payment Element
    elements,
    confirmParams: {
        return_url: 'https://8000-edenobrega-ecombookstor-adsi4kg0h9l.ws-eu54.gitpod.io/checkout/success',
    },
  });

  if (error) {
    // This point will only be reached if there is an immediate error when
    // confirming the payment. Show error to your customer (for example, payment
    // details incomplete)
    const messageContainer = document.querySelector('#error-message');
    messageContainer.textContent = error.message;
  } else {
    // Your customer will be redirected to your `return_url`. For some payment
    // methods like iDEAL, your customer will be redirected to an intermediate
    // site first to authorize the payment, then redirected to the `return_url`.
  }
});