const buttons = document.querySelectorAll('.subnav-btn');
const products = document.querySelectorAll('.product');

buttons.forEach(button => {
    button.addEventListener('click', function () {
        const filterTag = this.title;
        console.log("Filtering for:", filterTag);
        products.forEach(product => {
            const productTags = product.getAttribute('data-tags').split(' ');
            console.log(productTags);
            if (productTags.includes(filterTag)) {
                product.style.display = 'block';
            } else {
                product.style.display = 'none';
            }
        });
    });
});