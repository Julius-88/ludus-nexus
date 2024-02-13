const buttons = document.querySelectorAll('.subnav-btn');
const products = document.querySelectorAll('.product');

buttons.forEach(button => {
    button.addEventListener('click', function () {
        const filterTag = this.dataset.subnav;
        console.log("Filtering for:", filterTag);
        products.forEach(product => {
            try {
                const productTags = product.getAttribute('data-tags').split(' ');
                console.log(productTags);
                if (productTags.includes(filterTag)) {
                    product.style.display = 'block';
                } else {
                    product.style.display = 'none';
                }
            } catch (error) {
                console.error("Error processing product:", product, error);
            }
        });
    });
});