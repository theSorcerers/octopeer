require 'rails_helper'

RSpec.describe Api::MouseClickEventsController, type: :controller do
  describe "GET #index" do
    it "returns all mouse click events" do
      create_list :mouse_click_event, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one mouse click event" do
      mouse_click_event = create :mouse_click_event

      get :show, params: { id: mouse_click_event.id }

      expect(json[:id]).to eq(mouse_click_event.id)
      expect(json[:session][:id]).to eq(mouse_click_event.session_id)
    end
  end

  describe "POST #create" do
    it "creates a mouse click event" do
      session = create :session

      post :create,
           params: { mouse_click_event: { session_id: session.id,
                                          created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
