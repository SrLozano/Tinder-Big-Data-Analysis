# Big Data Analysis of Tinder 🗂 ❤️

Big Data analysis of the dating app Tinder. Done by **Mario Lozano Cortés**, Artificial Intelligence master's student at _Universitat Rovira i Virgili_ and _Universitat Politècnica de Catalunya · BarcelonaTech - UPC_. The resolution of this task is part of the Big Data Analytics course. **The goal of this project is to study and analyse the existence of differences in the behaviour of men and women in the use of the dating app Tinder**. To do so, the Big Data techniques learnt throughout the course will be used and Python and MongoDB will be employed as data manipulation and management tools.

## 🎯 Goal of the project

As previously stated, this **project's goal is to study and analyse the existence of differences in the behaviour of men and women in the use of the dating app Tinder**. As described by Wikipedia, _"Tinder is an online dating and geosocial networking application. In Tinder, users "swipe right" to like or "swipe left" to dislike other users' profiles, which include their photos, a short bio, and a list of their interests. Tinder uses a "double opt-in" system where both users must like each other before they can exchange messages"_.

The application makes use of a **freemium model**. Thus, the basic functionalities are free to use, while the advanced functionalities require a fee to be used. Some of the premium features are unlimited likes (100 in the basic version), super likes with messages, discovering who has liked your profile or highlighting your likes to other users. In this way, **the app must know how its users use each of the features in order to achieve the best possible business model**. Immediately, **we can distinguish two groups in the application, men and women** (as organised by the application itself). Thus, one of the first questions that arise is whether there are differences in the use of the application between the two groups. **This question is especially relevant for a correct segmentation of the market to offer an appropriate set of features to both men and women.**

In order to carry out the proposed analysis, **the following questions are defined** to be resolved throughout the analysis:

**Questions:**

-   _Who is more selective? Passes vs Likes by sex_
    
-   _Who recieves the more attention? Matches by sex_
    
-   _Who uses the app the most? App opens by sex_
    
-   _Who is most willing to pay for a subscription? Number of times the likes limit is reached per sex_
    
-   _Who talks the most? Messaging behaviour by sex_
    
-   _What is the minimum, mean and maximum percentage of one message-conversations for every sex? What about the number of ghostings after the initial message?_
    
-   _Who uses more instagram by sex?_
    
-   _More used emojis by sex_

## 💾 Data 
**[swipestats.io](https://www.swipestats.io/) provided the data at no cost for academic purposes**. swipestats is an anonymous data visualization and comparison web service that seeks to help people understand their Tinder data. For using the service a person must download its data from the Tinder app and upload it to swipestats to get interesting insights about their behaviour in the app.

**The dataset consists of a single JSON file (560MB) and none a single description or explanation of the data is given. Thus, the most crucial task of the analysis is to understand the data at hand** to be able to get valuable information from it.

## 🏅 Results

Throughout this study, the differences between the two predominant groups on Tinder, men and women, have been analysed. To do so, data provided by _swipestats.io_ from real users has been used, and an important descriptive and cleaning task has been carried out on the data, as it did not have any type of explanation and it contained redundancies in certain fields. In this way, the data exploration process has been carried out on each of the fields that made up the dataset and it has been managed and stored in a _NoSQL_ database, specifically _MongoDB_.

Among the insights discovered, the following stand out:

-   **Men give many more likes than women (x3.1 times).**
    
-   **Women ignore many more profiles than men (x1.4 times).**
    
-   **Women get many more matches than men (x2 times).**
    
-   **There is no significant difference between the number of times men and women log on to the application per day.**
    
-   **Men reach the daily likes limit many more times than women (x5.1 times).**
    
-   **There is no significant difference in the length of conversations between men and women.**
    
-   **Men tend to have a higher number of worse conversations as their percentage of single-message conversations is much higher than that of women (x1.4 times).**
    
-   **Women do much more ghosting than men (x2.7 times).**
    
-   **Women tend to link their Instagram profiles slightly more than men (26.67% women vs 21.45% men).**
    
-   **There are no major differences between the emojis used by men and women, with the two preferred emojis being the same for both sexes. The emojis used by men but not by women (in the Top 15 most common) are 😃, 😜, 🍷. The emojis used by women but not by men (in the Top 15 most common) are 😭, 🥺, 🙃.**
    

Therefore, it can be deduced that there are significant differences between men's and women's use of Tinder. **The data obtained support the hypothesis that women have a more selective pattern of dating behaviour than men**. This information is drawn from the fact that there are no significant differences in terms of the number of times the application is used per day, but there are significant differences in the ratio of profiles that are valid for a possible date (like + match + long enough conversation) between men and women.

Thus, **the assessment of the project is highly positive**, given that the proposed objectives have been met satisfactorily. A clear question has been defined, the necessary data have been obtained, appropriate management, exploration and cleaning have been proposed and a complete analysis has been carried out, which has provided valuable answers to the questions defined. Thus, **the extracted information is highly relevant for making business decisions concerning the freemium model** used in the app.

