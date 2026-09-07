---
title: 'Contact'
date: 2023-10-24
type: landing

design:
  spacing: '5rem'
  
sections:
  - block: contact-info
    content:
      title: Contact Us
      subtitle: Get in touch with our research team
      visit_title: Visit Our Lab
      connect_title: Connect With Us
      address:
        lines:
          - Smith Laboratory
          - Department of Computer Science
          - University of Excellence
          - 123 Science Drive
          - Excellence City, EC 12345
          - United States
      office_hours:
        - "Monday - Friday: 9:00 AM - 5:00 PM"
        - "Lab Meetings: Fridays 2:00 PM"
      email: lab@example.edu
      phone: "+1 (555) 123-4567"
      social:
        - icon: brands/x
          url: https://x.com/SmithLabResearch
        - icon: brands/linkedin
          url: https://linkedin.com/company/smith-lab
        - icon: brands/github
          url: https://github.com/smith-lab
      prospective:
        title: Prospective Members
        text: Interested in joining our lab? We're looking for motivated researchers.
        button:
          text: View Open Positions
          url: /opportunities
      map_url: https://maps.google.com/?q=University+of+Excellence
      show_form: false
    design:
      css_class: "bg-gray-50 dark:bg-gray-900"
      spacing:
        padding: ["3rem", 0, "3rem", 0]
        
  - block: map
    content:
      title: Visit the lab
      subtitle: We're on the Stanford campus — drop in any time during office hours.
      location:
        address: "353 Jane Stanford Way\nStanford, CA 94305\nUnited States"
        lat: 37.4275
        lng: -122.1697
      zoom: 15
      cta:
        directions:
          text: Get directions
        phone: +1-650-555-0142
        email: hello@example.com
    design:
      layout: side-by-side
      height: md
      style: streets

---