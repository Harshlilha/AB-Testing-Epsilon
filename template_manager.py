import os
from pathlib import Path
import shutil

def delete_template(category, template_name):
    """
    Delete a specific template from a category
    
    Args:
        category (str): The category folder name
        template_name (str): The name of the template file without .html extension
    
    Returns:
        bool: True if template was deleted successfully, False otherwise
    """
    base_dir = Path("templates/html_templates")
    template_path = base_dir / category / f"{template_name}.html"
    
    try:
        if template_path.exists():
            template_path.unlink()
            
            # Check if category folder is empty
            category_dir = template_path.parent
            if not any(category_dir.iterdir()):
                category_dir.rmdir()
                
            print(f"Successfully deleted template: {category}/{template_name}.html")
            return True
        else:
            print(f"Template not found: {category}/{template_name}.html")
            return False
    except Exception as e:
        print(f"Error deleting template: {str(e)}")
        return False

def list_templates():
    """
    List all available templates grouped by category
    
    Returns:
        dict: Dictionary of categories and their templates
    """
    base_dir = Path("templates/html_templates")
    templates = {}
    
    if base_dir.exists():
        for category_dir in base_dir.iterdir():
            if category_dir.is_dir():
                category = category_dir.name
                templates[category] = [
                    template.stem for template in category_dir.glob("*.html")
                ]
    
    return templates

def create_template_structure():
    # Base directory for templates
    base_dir = Path("templates/html_templates")
    
    # Categories with their respective templates
    categories = {
        "ecommerce": [
            ("product_page", "Product Details Page"),
            ("category_listing", "Category Products Listing"),
            ("shopping_cart", "Shopping Cart Page"),
            ("checkout_page", "Checkout Process"),
            ("order_confirmation", "Order Confirmation"),
            ("account_dashboard", "Customer Account Dashboard")
        ],
        "holiday": [
            ("christmas_special", "Christmas Special"),
            ("new_year_celebration", "New Year Celebration"),
            ("thanksgiving_event", "Thanksgiving Event"),
            ("halloween_party", "Halloween Party"),
            ("easter_celebration", "Easter Celebration"),
            ("valentines_special", "Valentine's Special")
        ],
        "events_invitations": [
            ("corporate_gala", "Corporate Gala Night"),
            ("product_launch_event", "Product Launch Event"),
            ("networking_mixer", "Professional Networking Mixer"),
            ("workshop_seminar", "Workshop & Seminar"),
            ("award_ceremony", "Awards Ceremony"),
            ("conference_summit", "Conference & Summit")
        ],
        "deals_offers": [
            ("limited_time", "Limited Time Offers"),
            ("premium_deals", "Premium Member Deals"),
            ("special_bundles", "Special Bundle Offers"),
            ("clearance_sale", "Clearance Sale Deals"),
            ("combo_deals", "Combo Deals & Savings"),
            ("exclusive_offers", "Exclusive VIP Offers")
        ],
        "business": [
            ("company_overview", "Company Overview"),
            ("investment_proposal", "Investment Proposal"),
            ("quarterly_report", "Quarterly Business Report"),
            ("business_pitch", "Business Pitch Deck"),
            ("market_analysis", "Market Analysis Report"),
            ("annual_report", "Annual Report Summary")
        ],
        "announcement": [
            ("product_launch", "New Product Launch"),
            ("brand_refresh", "Brand Refresh Unveiling"),
            ("milestone", "Company Milestone Celebration"),
            ("collaboration", "Strategic Collaboration"),
            ("award_win", "Award Recognition"),
            ("innovation_launch", "Innovation Announcement"),
            ("achievement", "Achievement Announcement"),
            ("brand_launch", "Brand Launch Announcement"),
            ("expansion_news", "Business Expansion News"),
            ("partnership", "Partnership Announcement"),
            ("store_opening", "Store Opening Announcement"),
            ("website_redesign", "Website Redesign Announcement")
        ],
        "black_friday": [
            ("mega_deal", "Black Friday Mega Deals"),
            ("vip_early_access", "VIP Early Access Sale"),
            ("cyber_monday_tech", "Cyber Monday Tech Bonanza"),
            ("flash_sale", "Flash Sale Alert"),
            ("countdown_deals", "Countdown Deals Spectacular"),
            ("exclusive_bundle", "Exclusive Black Friday Bundles")
        ],
        "newsletter": [
            ("monthly_update", "Monthly Newsletter"),
            ("product_launch", "New Product Announcement"),
            ("company_news", "Company Updates"),
            ("industry_insights", "Industry Insights"),
            ("success_stories", "Customer Success Stories"),
            ("upcoming_events", "Upcoming Events")
        ],
        "promotional": [
            ("summer_sale", "Summer Sale Spectacular"),
            ("holiday_special", "Holiday Special Offers"),
            ("clearance", "Clearance Sale"),
            ("bundle_deal", "Bundle and Save"),
            ("loyalty_rewards", "Loyalty Member Rewards"),
            ("new_collection", "New Collection Launch")
        ],
        "feedback": [
            ("customer_satisfaction", "Customer Satisfaction Survey"),
            ("product_review", "Product Review Request"),
            ("service_feedback", "Service Experience Feedback"),
            ("post_purchase", "Post-Purchase Follow-up"),
            ("website_feedback", "Website Experience Survey"),
            ("nps_survey", "NPS Survey")
        ],
        "survey": [
            ("market_research", "Market Research Survey"),
            ("preference_survey", "Customer Preference Study"),
            ("brand_awareness", "Brand Awareness Survey"),
            ("demographic_study", "Demographic Study"),
            ("feature_request", "Product Feature Survey"),
            ("exit_survey", "Exit Survey")
        ],
        "quizzes": [
            ("product_quiz", "Product Recommendation Quiz"),
            ("knowledge_test", "Industry Knowledge Test"),
            ("style_finder", "Personal Style Finder"),
            ("preference_match", "Preference Matching Quiz"),
            ("personality_test", "Brand Personality Test"),
            ("engagement_quiz", "Customer Engagement Quiz")
        ],
        "sales": [
            ("end_of_season", "End of Season Sale"),
            ("inventory_clearance", "Inventory Clearance"),
            ("members_only", "Members Only Sale"),
            ("weekend_special", "Weekend Special"),
            ("flash_deals", "24-Hour Flash Deals"),
            ("bulk_discount", "Bulk Purchase Discount")
        ],        "deals_offers": [
            ("limited_time", "Limited Time Offers"),
            ("premium_deals", "Premium Member Deals"),
            ("special_bundles", "Special Bundle Offers"),
            ("clearance_sale", "Clearance Sale Deals"),
            ("combo_deals", "Combo Deals & Savings"),
            ("exclusive_offers", "Exclusive VIP Offers")
        ],
        "seasonal": [
            ("spring_collection", "Spring Collection"),
            ("summer_essentials", "Summer Essentials"),
            ("fall_fashion", "Fall Fashion Preview"),
            ("winter_sale", "Winter Wonderland Sale"),
            ("holiday_gift", "Holiday Gift Guide"),
            ("new_year", "New Year New Deals")
        ],
        "blog_updates": [
            ("featured_articles", "Featured Articles Roundup"),
            ("latest_posts", "Latest Blog Posts"),
            ("monthly_digest", "Monthly Content Digest"),
            ("tech_insights", "Technology Insights"),
            ("industry_news", "Industry News Roundup"),
            ("success_stories", "Customer Success Stories")
        ],
        "announcement": [
            ("product_launch", "New Product Launch"),
            ("brand_refresh", "Brand Refresh Unveiling"),
            ("milestone", "Company Milestone Celebration"),
            ("collaboration", "Strategic Collaboration"),
            ("award_win", "Award Recognition"),
            ("innovation_launch", "Innovation Announcement"),
            ("achievement", "Achievement Announcement"),
            ("brand_launch", "Brand Launch Announcement"),
            ("expansion_news", "Business Expansion News"),
            ("partnership", "Partnership Announcement"),
            ("store_opening", "Store Opening Announcement"),
            ("website_redesign", "Website Redesign Announcement")
        ],
        "business": [
            ("company_overview", "Company Overview"),
            ("investment_proposal", "Investment Proposal"),
            ("quarterly_report", "Quarterly Business Report"),
            ("business_pitch", "Business Pitch Deck"),
            ("market_analysis", "Market Analysis Report"),
            ("annual_report", "Annual Report Summary")
        ]
    }

    # Create base template with CSS and JS
    def create_base_template(title, category_type, template_type):
        content_html = generate_content(category_type, template_type)
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Reset styles */
        body {{
            margin: 0;
            padding: 0;
            font-family: 'Poppins', sans-serif;
            line-height: 1.6;
            background-color: #f5f5f5;
        }}
        
        .container {{
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
        }}
        
        .header {{
            background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
            color: white;
            padding: 30px 20px;
            text-align: center;
            border-radius: 8px 8px 0 0;
        }}
        
        .content {{
            padding: 30px 20px;
        }}
        
        .button {{
            display: inline-block;
            padding: 12px 24px;
            background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%);
            color: white;
            text-decoration: none;
            border-radius: 6px;
            font-weight: bold;
            margin: 20px 0;
            transition: transform 0.2s;
        }}
        
        .button:hover {{
            transform: translateY(-2px);
        }}
        
        .footer {{
            background-color: #f8f9fa;
            padding: 20px;
            text-align: center;
            border-radius: 0 0 8px 8px;
            color: #6b7280;
            font-size: 0.9em;
        }}

        .highlight {{
            background: #fef3c7;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: bold;
        }}
        
        /* Category-specific styles */        .black_friday {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); color: white; }}
        .newsletter {{ background: linear-gradient(135deg, #0ea5e9 0%, #0284c7 100%); }}
        .promotional {{ background: linear-gradient(135deg, #f43f5e 0%, #e11d48 100%); }}
        .feedback {{ background: linear-gradient(135deg, #8b5cf6 0%, #7c3aed 100%); }}
        .survey {{ background: linear-gradient(135deg, #10b981 0%, #059669 100%); }}
        .quizzes {{ background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); }}
        .sales {{ background: linear-gradient(135deg, #ec4899 0%, #db2777 100%); }}
        .seasonal {{ background: linear-gradient(135deg, #6366f1 0%, #4f46e5 100%); }}
        .announcement {{ background: linear-gradient(135deg, #14b8a6 0%, #0d9488 100%); }}
        .blog_updates {{ background: linear-gradient(135deg, #818cf8 0%, #6366f1 100%); }}
        .business {{ background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%); }}
        
        /* Responsive design */
        @media only screen and (max-width: 600px) {{
            .container {{
                width: 100%;
                padding: 10px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header {category_type}">
            <h1>{title}</h1>
        </div>
        
        <div class="content">
            {content_html}
        </div>
        
        <div class="footer">
            <p>© 2025 Your Company Name. All rights reserved.</p>
            <p>
                <a href="#" style="color: #6b7280; text-decoration: underline;">Unsubscribe</a> | 
                <a href="#" style="color: #6b7280; text-decoration: underline;">Privacy Policy</a>
            </p>
        </div>
    </div>

    <script>
        // Add interactivity if needed
        document.addEventListener('DOMContentLoaded', function() {{
            // Add any necessary JavaScript functionality
            const buttons = document.querySelectorAll('.button');
            buttons.forEach(button => {{
                button.addEventListener('mouseover', () => {{
                    button.style.transform = 'translateY(-2px)';
                }});
                button.addEventListener('mouseout', () => {{
                    button.style.transform = 'translateY(0)';
                }});
            }});
        }});
    </script>
</body>
</html>'''

    def generate_content(category_type, template_type):
        # Content templates for different categories
        content_templates = {
            "black_friday": {
                "mega_deal": '''
                    <div class="flash-sale-banner">
                        <div class="flash-icon">⚡</div>
                        <h2 class="animate__animated animate__heartBeat">BLACK FRIDAY MEGA DEALS</h2>
                        <div class="timer" id="countdown">Ends in: <span id="timer">23:59:59</span></div>
                    </div>
                    
                    <div class="deals-grid">
                        <div class="deal-card animate__animated animate__fadeInLeft">
                            <div class="discount-tag">70% OFF</div>
                            <h3>Premium Electronics</h3>
                            <p>Latest gadgets at unbeatable prices</p>
                            <div class="original-price">$999</div>
                            <div class="sale-price">$299</div>
                        </div>
                        
                        <div class="deal-card animate__animated animate__fadeInRight">
                            <div class="discount-tag">BOGO</div>
                            <h3>Fashion & Accessories</h3>
                            <p>Buy one get one free on all items</p>
                            <div class="special-offer">Limited Stock!</div>
                        </div>
                    </div>
                    
                    <div class="features-list">
                        <div class="feature">
                            <span class="feature-icon">🚚</span>
                            <span>Free Express Shipping</span>
                        </div>
                        <div class="feature">
                            <span class="feature-icon">💳</span>
                            <span>Buy Now, Pay Later</span>
                        </div>
                        <div class="feature">
                            <span class="feature-icon">🎁</span>
                            <span>Free Gift Wrapping</span>
                        </div>
                    </div>
                    
                    <div class="cta-section">
                        <p class="highlight animate__animated animate__pulse">⏰ Don't Wait! Offer ends in <span id="timer2">23:59:59</span></p>
                        <a href="#" class="mega-button">SHOP NOW</a>
                        <p class="terms">*Terms and conditions apply</p>
                    </div>
                ''',
                "vip_early_access": '''
                    <h2>🌟 Exclusive VIP Early Access</h2>
                    <p>Dear VIP Customer,</p>
                    <p>Get ahead of the crowd with exclusive early access to our Black Friday deals!</p>
                    <p class="highlight">24 hours before everyone else</p>
                    <a href="#" class="button">Access Early Deals</a>
                '''
            },
            "newsletter": {
                "monthly_update": '''
                    <h2>📰 Your Monthly Update Is Here</h2>
                    <p>Inside this month's newsletter:</p>
                    <ul>
                        <li>Company highlights</li>
                        <li>New product launches</li>
                        <li>Customer success stories</li>
                        <li>Upcoming events</li>
                    </ul>
                    <a href="#" class="button">Read More</a>
                '''
            },
            "promotional": {
                "summer_sale": '''
                    <h2>☀️ Summer Sale Spectacular!</h2>
                    <p>Heat up your summer with these amazing deals:</p>
                    <ul>
                        <li>Up to 50% off summer essentials</li>
                        <li>Free shipping on orders over $50</li>
                        <li>Special bundle offers</li>
                    </ul>
                    <a href="#" class="button">Shop Summer Sale</a>
                '''
            }
        }
        
        # Default content if specific template not found
        default_content = f'''
            <h2>Welcome!</h2>
            <p>Thank you for being a valued customer.</p>
            <p>We have some exciting news to share with you.</p>
            <a href="#" class="button">Learn More</a>
        '''
        
        return content_templates.get(category_type, {}).get(template_type, default_content)

    # Create directory structure and templates
    for category, templates in categories.items():
        category_dir = base_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)
        
        for template_name, title in templates:
            template_path = category_dir / f"{template_name}.html"
            template_content = create_base_template(title, category, template_name)
            
            with open(template_path, "w", encoding="utf-8") as f:
                f.write(template_content)
            
            print(f"Created template: {category}/{template_name}.html")

if __name__ == "__main__":
    # Example usage:
    # 1. Create all templates
    create_template_structure()
    
    # 2. List all templates
    templates = list_templates()
    for category, template_list in templates.items():
        print(f"\n{category}:")
        for template in template_list:
            print(f"  - {template}")
    
    # 3. Example: Delete a specific template (commented out to prevent accidental deletion)
    # delete_template("ecommerce", "product_page")