import string
import random
from flask import jsonify
from model import db, URL
from datetime import datetime


class URLShortener:
    def __init__(self):
        pass
    
    @staticmethod
    def validate_shortcode(shortcode):
        """This function validates the shortcode"""
        if len(shortcode) != 6:
            return False
        for characters in shortcode:
            if characters not in string.ascii_letters + string.digits + '_':
                return False
        return True
    
    @staticmethod
    def generate_shortcode():
        """This function generates a random shortcode."""
        characters = '_' + string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(6))

    @staticmethod
    def shortcode_is_used(shortcode):
        """Checks if a shortcode is already in use"""
        url_record = URL.query.filter_by(shortcode=shortcode).first()
        return url_record is not None
    
    def shorten_url(self, request):
        """Shorten a URL and return the shortcode."""
        data = request.get_json()
        original_url = data.get('url')
        shortcode = data.get('shortcode')
        if not original_url:
            return jsonify({"400": "URL is not present"}), 400
        if shortcode:
            if not self.validate_shortcode(shortcode):
                return jsonify({"412": "The provided shortcode is invalid"}), 412
            if self.shortcode_is_used(shortcode):
                return jsonify({"409": "The provided shortcode is already in use"}), 409
        else:
            shortcode = self.generate_shortcode()
            while self.shortcode_is_used(shortcode):
                shortcode = self.generate_shortcode()

        url_entry = URL(original_url=original_url, shortcode=shortcode)
        db.session.add(url_entry)
        db.session.commit()
        return jsonify({"shortcode": shortcode}), 201

    def redirect_url(self, shortcode):
        """Redirect to the original URL."""
        url_entry = URL.query.filter_by(shortcode=shortcode).first()
        if url_entry:
            url_entry.redirect_count += 1
            url_entry.last_redirect = datetime.now()
            db.session.commit()
            return jsonify({"location": url_entry.original_url}), 302
        else:
            return jsonify({"404": "Shortcode not found"}), 404
        
    @staticmethod
    def get_stats(shortcode):
        """This function returns the stats of a URL."""
        url_entry = URL.query.filter_by(shortcode=shortcode).first()
        if url_entry:
            stats = {
                "created": url_entry.creation_date.isoformat(),
                "lastRedirect": url_entry.last_redirect.isoformat() if url_entry.last_redirect else None,
                "redirectCount": url_entry.redirect_count
            }
            
            return jsonify(stats), 200
        else:
            return jsonify({"404": "Shortcode not found"}), 404
        

