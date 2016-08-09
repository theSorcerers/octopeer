require 'rails_helper'

RSpec.describe Api::HtmlPagesController, type: :controller do
  describe "GET #index" do
    it "returns all html pages" do
      create_list :html_page, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one html page" do
      html_page = create :html_page

      get :show, params: { id: html_page.id }

      expect(json[:id]).to eq(html_page.id)
      expect(json[:session][:id]).to eq(html_page.session_id)
      expect(json[:dom]).to eq(html_page.dom)
    end
  end

  describe "POST #create" do
    it "creates a html page" do
      session = create :session

      post :create,
           params: { html_page: { session_id: session.id,
                                  dom: '<!DOCTYPE html><html></html>',
                                  created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(json[:dom]).to eq('<!DOCTYPE html><html></html>')
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
