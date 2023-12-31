# Ludus Nexus: The Console Gaming Hub
Ludus Nexus is the go-to destination for console gamers, gaming novices, and anyone looking to find the perfect gaming-related gift. Our site is dedicated to simplifying your search for information, games, accessories, and the latest in console gaming. Designed for clarity and ease of navigation, we bring the vast gaming landscape right to your fingertips.

## For Gamers and Beyond
Ludus Nexus caters to the needs of avid gamers and casual visitors alike. We aim to create an inviting environment where discovering your next gaming experience or locating the ideal accessory is both straightforward and enjoyable. Our platform is a testament to our belief in a user-friendly experience that welcomes everyone, no matter their level of engagement with gaming.

# Core Revenue Stream
## Direct Sales
Ludus Nexus specializes in the sale of gaming consoles, video games, and gaming accessories. We generate revenue primarily through the direct online sale of these products. We ensure a competitive pricing model and a diverse range of products to cater to a broad gaming audience.

# Original Design Concept

The following design is the initial concept and starting point for the Ludus Nexus project. As we are using an agile development process, the final implementation of this site may differ from the original design concept. This flexibility allows us to adapt and refine the design based on user feedback and evolving project requirements.

The design in Figma, which can be viewed [here](https://www.figma.com/file/hGDWtjoOtL00DrgiPRRoCf/Ludus-Nexus?type=design&node-id=0%3A1&mode=design&t=1MBSYz7Agfgsb057-1), showcases the main user journey, with minor interactions detailed during the development phase. You can explore the basic idea of how the website should work on PC [here](https://www.figma.com/proto/hGDWtjoOtL00DrgiPRRoCf/Ludus-Nexus?type=design&node-id=102-2&t=lmn1KUorCpUhJ1QG-0&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=102%3A2&show-proto-sidebar=1), and see what it would look like on mobile [here](https://www.figma.com/proto/hGDWtjoOtL00DrgiPRRoCf/Ludus-Nexus?type=design&node-id=548-537&t=lmn1KUorCpUhJ1QG-0&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=548%3A537&show-proto-sidebar=1).

## Inspiration

The design draws inspiration from prominent gaming and technology websites, including:

- [inet](https://www.inet.se/)
- [webhallen](https://www.webhallen.com/)
- [Nintendo](https://www.nintendo.se/)
- [Playstation](https://www.playstation.com/sv-se/)
- [Xbox](https://www.xbox.com/sv-SE)
- [Youtube](https://www.youtube.com/)

These sources were instrumental in shaping the aesthetic and functional aspects of Ludus Nexus, providing insights into successful layouts and features that resonate with gaming audiences.

## Color Palette

The selected color palette reflects the essence of gaming culture, balancing visual appeal with functionality:

### Default setting - Dark Mode
- Background: Black (000000) for depth and focus.
- Text & Items Background: White (FFFFFF) for stark contrast and readability.
- Placeholder Text & HR: Grey (E5E5E5) for subtlety and clarity.
- Input Fields: Eerie Black (242526) for a sleek, modern look.

![Dark Mode](./static/img/dark-mode.png)

### Light Mode
- Background: Grey (E5E5E5) for a softer, eye-friendly backdrop.
- Text: Black (000000) for sharp contrast and focus on content.
- Items & Input fields: White (FFFFFF) for a clean and clear interface.
- Placeholder Text & HR: Black Olive (42413C) for a subtle yet distinct appearance.

![Light Mode](./static/img/light-mode.png)

### CTA
- CTA Colors: Veronica (9747FF) as the primary color, transitioning to Amethyst (A367F2) on hover for interactivity.

### Console Color Integration

The design embraces the vibrant identities of the selected gaming consoles by integrating their signature colors into our site's interface, enhancing user navigation and providing an instantly familiar experience for fans of each platform:

- PlayStation Blue (#0070CC) for primary display, transitioning to PlayStation Hover Blue (#218DE5) upon hover.
- Xbox Green (#107B10) for primary display, transitioning to Xbox Hover Green (#228822) upon hover.
- Nintendo Red (#E60012) for primary display, transitioning to Nintendo Hover Red (#E71B2B) upon hover.

![CTA and Console Colors](./static/img/cta-console-colors.png)

# Design Updates
These updates are part of our continuous effort to improve user experience and website aesthetics.
1. **Mobile View Navbar:** Implemented hamburger menu functionality for a more user-friendly experience in mobile view. This replaced the previous design of circular navigation links.
2. **Navigation Menu Color in Light Mode:** Adjusted the color scheme of the navigation menu in light mode to ensure a more seamless integration with the overall page design. 
3. **Removal of Home Icon in Navbar:** After reviewing similar websites in the industry, it became apparent that a dedicated home icon is not a common practice. Most sites rely on their brand logo or name in the header to function as a home link. In aligning with these industry standards and to simplify the user interface, the decision was made to remove the home icon from our navigation. This change is expected to streamline the user experience while maintaining intuitive navigation by using our brand name in the header as the primary method to return to the home page.
4. **Updating Footer Links - Privacy Policy:** The footer links for cookies and GDPR have been consolidated into a single Privacy Policy link. This change was made to streamline the footer's content, as we do not use cookies and all GDPR-related information is comprehensively addressed in our Privacy Policy. This adjustment simplifies user access to essential privacy information.
5. **Removal of Facebook Icon from Footer:** Upon evaluating several reference pages within the industry, a common trend was observed where websites typically opt for either a Facebook logo or the text in their footer, but not both. To align with these standards and to ensure a cleaner, more streamlined user interface, we decided to remove the Facebook icon from our footer. Our footer now features only the text link to our Facebook page, simplifying the design while retaining the essential function of directing users to our social media presence.
6. **Integration of a Modal for Newsletter Subscription in the Footer:** The design was updated to include a modal-trigger button for newsletter subscriptions, replacing the direct input field in the footer. This change was made to ensure a cohesive and uniform design. The modal provides a focused and user-friendly interface for newsletter sign-up, enhancing the overall user experience."
7. **Reintroduction of Home Icon after user testing:** The home icon was re-added to the navigation for enhanced user accessibility and intuitive navigation, especially for users less familiar with web conventions. Recognizing that not all users may intuitively click on the header to return to the home page, the home icon provides a clear, alternative navigation option. Additionally, the header links on each console page have been updated to correspond to their specific pages, improving the user experience in the mobile version where the main navigation is hidden behind a hamburger menu." 

## Fonts
- The Griffy font has been chosen for the sites title name, this is to stand out from other sites and give a memorable impression on the user.
- The Poppins font has been chosen for Playstation and Xbox titles, this is because this font resembles these branches font the most.
- The Didact Gothic font has been chosen for the Nintendo title, this is because this font resembles the Nintendo font the most.
- The Raleway font has been chosen for the overall content. It seems to match well with all the font types while still standing out.

# Database Schema
The database schema depicted below outlines the foundational structure of the Ludus Nexus e-commerce platform, detailing how various data elements such as users, products, and events are interconnected. This schema serves as a blueprint for the database's initial development, with the understanding that alterations may occur as the project evolves to accommodate new requirements or improvements.

![Database Schema](./static/img/database-schema.JPG)

1. **Users**: This table holds essential data about the users of the platform, such as their login credentials and contact information. It's the central point for managing user accounts and is linked to **Orders**, **EventNotifications**, and **WishList**. Allowing for functionalities like tracking order history, managing event interests, and saving favorite products.

2. **Products**: Contains detailed information about each product available on the platform, including names, descriptions, prices, and associated console types. It's linked to the **Consoles** table for categorizing products by their respective gaming consoles, enhancing user navigation and product discovery. It also connects to **OrderDetails** for order processing and **WishList** allowing users to bookmark their favorite items.

3. **Consoles**: Categorizes products based on console types like PlayStation, Xbox or Nintendo. Each entry in this table represents a different gaming console, and it's linked to **Products** to facilitate easy filtering of products based on the console type, thereby improving the user shopping experience.

4. **Orders** and **OrderDetails**: The **Orders** table manages the processing of user orders, recording essential details like order dates and total prices. The **OrderDetails** table complements this by tracking individual products within each order, including quantities and specific product IDs, ensuring accurate order fulfillment and inventory management.

5. **EventNotifications**: This table connects users with upcoming gaming events they're interested in. It links to the **Events** table and stores information about which events users want to be notified about, enabling personalized event reminders and updates.

6. **Events**: Stores comprehensive details about various gaming events, such as event names, dates, locations, and descriptions. This table is crucial for the event notification system, providing the necessary information to inform users about upcoming events that align with their interests.

7. **ProductTags** and **Tags**: These tables work together to provide a dynamic tagging system for products. **Tags** contains different labels like genres or age ratings, while **ProductTags** links these labels to specific products. This system is essential for features like product surveys, where users receive recommendations based on selected tags, and for general product categorization on the platform.

8. **NewsArticles**: Manages the display of news articles on the platform. It stores information about each article. This table is key for keeping users informed about the latest news in the gaming world, enhancing the platform's content richness.

9. **WishList**: Allows users to save products to a personal wishlist for future reference. It links to both **Users** and **Products** tables, enabling users to easily access and manage a list of products they are interested in purchasing or reviewing later.

# Update to Database

**ProductTags** has been removed in favor of Django's *ManyToManyField* in **Tags**, simplifying the management of product-tag relationships.

# Facebook Page

We are excited to introduce the official Facebook page for Ludus Nexus! This is where you'll get updates on the latest in gaming and find out about special promotions for PlayStation, Xbox, and Nintendo games and gear. Stay connected and catch the best deals by following us on our Facebook page.

[Click here to visit Facebook page](https://www.facebook.com/profile.php?id=61553536475742)

Below are images showcasing the Facebook page and the dedicated business Gmail account, which is set up for customer support and inquiries:

**Top of Facebook Page**

![Facebook images](./static/img/facebook-page-p1.JPG)

**Middle of Facebook Page**

![Facebook images](./static/img/facebook-page-p2.JPG)

**Bottom of Facebook Page**

![Facebook images](./static/img/facebook-page-p3.JPG)

**Gmail Account**

![Gmail Account](./static/img/gmail-account.JPG)

**Call to Action (CTA) on Facebook:** This feature was not implemented. While exploring options for adding a CTA button on Facebook, I encountered several choices. However, it was unclear whether these options would incur charges, and none matched the straightforward approach demonstrated in the tutorial video. To avoid potential costs and complexity, I decided not to implement a Facebook CTA button at this stage.

![Choosing a CTA button on Facebook](./static/img/facebook-cta.JPG)


# Features
## Privacy Policy Modal

To enhance user convenience and transparency, a Privacy Policy modal has been integrated into the footer of the site. This allows users to access information about our privacy practices and GDPR compliance without navigating away from the current page. The policy was generated using[Privacy Policy Generator](https://www.privacypolicygenerator.info/), ensuring comprehensive coverage of key privacy aspects.


**Privacy Policy Button**

![Privacy Policy Button](./static/img/privacy-policy-button.JPG) 

**Privacy Policy Modal**

![Privacy Policy Opened](./static/img/privacy-policy-opened.JPG)

## 404 Error Page
Our website includes a custom 404 error page designed to clearly communicate to users when they have encountered a non-existent page or a broken link. The page features a clear and concise message, "PAGE NOT WORKING," ensuring users are immediately aware of the error.
The 404 page also includes a prominent Home button. This feature allows users to easily navigate back to the main content of the site.

## Newsletter Signup
A user-friendly newsletter signup modal has been integrated into the footer. This modal enables visitors to subscribe to our newsletter easily.

![Newsletter button](./static/img/newsletter-button.JPG)

**Registration Process:** Users can enter their email address in the modal to subscribe.

![Sign up modal](./static/img/newsletter-modal.JPG)

**Feedback on Subscription:**

- A confirmation message appears for successful signups.

![Success Message](./static/img/newsletter-success.JPG)

- An alert notifies users if they are already subscribed.

![Already Subscribed](./static/img/newsletter-existing.JPG)

- An error message is displayed for invalid email inputs.

![Error Message](./static/img/newsletter-invalid.JPG)

- A prompt indicates if the email field is left empty.

![Required Message](./static/img/newsletter-emptyfield.JPG)

In addition to the frontend features, all subscriptions are conveniently managed and visible in the MailChimp database, allowing for efficient user engagement and communication tracking.

![Mailchimp database](./static/img/newsletter-database.JPG)

# Theme Change
To enhance user experience, our website remembers the user's theme preference across browsing sessions. This is achieved by utilizing the browser's localStorage feature:

**Local Storage for Preferences**: When a user selects a theme, their choice is saved in the browser’s local storage. This means the next time they visit the website, it will automatically display their preferred theme, providing a consistent and personalized experience.

**No Login Required**: This functionality works without the need for user accounts or logging in, ensuring ease of use and immediate personalization for every visitor.

**Privacy-Friendly**: The use of local storage means that the theme preference is stored locally on the user's device, respecting their privacy and not requiring any server-side data storage or processing.

This simple yet effective use of local storage ensures that users enjoy a tailored browsing experience every time they visit our site.

![Dark Theme](./static/img/theme-dark.JPG)
![Light Theme](./static/img/theme-light.JPG)

# Products
Visitors to Ludus Nexus can easily explore a wide range of gaming products tailored for Playstation, Xbox, and Nintendo, directly accessible from the navbar.

## Efficient Navigation & Detailed Insights:

- **Subcategories:** Each product page can be neatly categorized into three sections: Games, Consoles, and Accessories, offering a streamlined browsing experience. Allowing users to filter the displayed products, makes it easier to find items aligned with their interests.

![Playstation Product Page](./static/img/playstation-product-page.JPG)

- **Product Descriptions:** Each product features a "Describe" button. Clicking on this provides a concise description, offering insights into the product's features and appeal.

![Description Button](./static/img/description-btn.JPG)

- **Product Header:** The header dynamically adjusts based on the current page, ensuring a seamless experience across devices in addition to enabling the mobile users to reset the view and see all available products with ease.

![Xbox Header](./static/img/xbox-product-page.JPG)

![Nintendo Header Mobile](./static/img/nintendo-product-page.JPG)

# Staff Registration and Management

**Staff:** A staff can be registered by an existing admin. This registration can only be done from Django Admin Panel.

![User Creation](./static/img/admin-creation.JPG)

Once the user is created, you are directed to a more detailed view, where you can add more user detail and which permissions they should have. An admin group has been created with full priviledge. More groups can be made with specific permissions if needed.

![User Detail](./static/img/admin-user-detail.JPG)
![User Detail Two](./static/img/admin-user-detail2.JPG)

The staff member can log-in to their account through the website via the regular login button in the navbar which users also have access to. The sign-in also has a remember me tickbox.

![Sign In](./static/img/sign-in-page.JPG)

Once they are logged in, they can access the Django Admin panel via the previous login button that has now become an account button. The admin panel inside the account button is only available to staff members.

![Admin Panel](./static/img/admin-panel.JPG)

Once logged in depending on their permissions they have access to all content through the databases.

![Admin Databases](./static/img/admin-database.JPG)
![Add Product](./static/img/add-product.JPG)

All changes made will show immediately on page.

![Added Product](./static/img/added-product.JPG)

# User Experience

The initial interface presents an overview of the site, encouraging new users to create accounts for a personalized experience.
Essential links like the privacy policy, contact information, and newsletter signup are located in the footer for easy access.

![Home Page](./static/img/home-page.JPG)

Users can select from Playstation, Xbox, or Nintendo categories via the navbar. Each product section includes subcategories for Games, Consoles, and Accessories, with filtering functionality.

The shopping cart icon in the navbar changes to purple when items are added, signaling items in the cart.

![Shopping Cart Icon](./static/img/shopping-cart-icon.JPG)

The shopping bag page allows users to review their selections, adjust quantities, remove items, and see the subtotal for each product and the total cost.

![Shopping](./static/img/shopping.JPG)

![Shopping Bag](./static/img/shopping-bag.JPG)

![Shopping Bag Two](./static/img/shopping-bag2.JPG)

A straightforward checkout process where users fill in shipping details.

![Checkout](./static/img/checkout.JPG)

Stripe integration is used for secure payment processing. The interface provides feedback for successful transactions and input errors.

![Payment](./static/img/payment.JPG)

![Success](./static/img/success.JPG)

![Success Stripe](./static/img/success-payment.JPG)

![Input Error](./static/img/error.JPG)

Post-purchase, users receive an order confirmation with a unique order number. Registered users can access their order history and receipts.

![Receite](./static/img/receites.JPG)

![Receite](./static/img/receites2.JPG)

The site includes functionalities for account management, including logout, viewing past orders, and account deletion, with confirmation prompts for safety.

![Sign Out](./static/img/signout.JPG)

![Delete Account](./static/img/delete.JPG)

The sign-in page provides options for new account creation and password recovery.

![Sign In](./static/img/signin.JPG)







# Unfixed Bugs
1. **Mailchimp Subscription Messages Bug:** The Mailchimp subscription form messages (success, error, etc.) do not reset after the modal is closed; they persist until the page is fully reloaded. Despite attempts to override Mailchimp's JavaScript functionality to reset these messages, the issue remains unresolved. The bug has been acknowledged and requires further investigation.

![Mailchimp code](./static/img/mailchimp-bug.JPG)

2. **Favicon.io - 401 Error Issue:** Recently, the favicon icons for the website have stopped loading, and a "401 Error" is being displayed in the browser's console. This issue occurred without any known changes to the static files or their configurations in Django.
This error prevents the favicon from being displayed in browser tabs, impacting the visual identification of the site.
The issue is under investigation, and a solution has not yet been implemented.

# Resources
- **Favicon.io**: Used for generating favicon images. [favicon.io](https://favicon.io/favicon-converter/)
- **FontAwesome**: Provides various icons used across the site. [fontawesome.com](https://fontawesome.com/)
- **Bootstrap v4.6**: Primary CSS framework used for designing the website. [getbootstrap.com](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
- **JQuery**: Utilized for JavaScript coding enhancements. [jquery.com](https://jquery.com/)
- **Stripe**: Using Stripe as a payment system. [Stripe](https://stripe.com/docs)