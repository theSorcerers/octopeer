require 'rails_helper'

RSpec.describe Api::ChangeTabEventsController, type: :controller do
  describe "GET #index" do
    it "returns all change tab events" do
      create_list :change_tab_event, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one change tab event" do
      change_tab_event = create :change_tab_event

      get :show, params: { id: change_tab_event.id }

      expect(json[:id]).to eq(change_tab_event.id)
      expect(json[:session][:id]).to eq(change_tab_event.session_id)
      expect(json[:url]).to eq(change_tab_event.url)
    end
  end

  describe "POST #create" do
    it "creates a change tab event" do
      session = create :session

      post :create,
           params: { change_tab_event: { session_id: session.id,
                                         url: 'http://octopeer.com/',
                                         created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(json[:url]).to eq('http://octopeer.com/')
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
