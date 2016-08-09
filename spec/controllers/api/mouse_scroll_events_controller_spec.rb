require 'rails_helper'

RSpec.describe Api::MouseScrollEventsController, type: :controller do
  describe "GET #index" do
    it "returns all mouse scroll events" do
      create_list :mouse_scroll_event, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one mouse scroll event" do
      mouse_scroll_event = create :mouse_scroll_event

      get :show, params: { id: mouse_scroll_event.id }

      expect(json[:id]).to eq(mouse_scroll_event.id)
      expect(json[:session][:id]).to eq(mouse_scroll_event.session_id)
      expect(json[:viewport_x]).to eq(mouse_scroll_event.viewport_x)
      expect(json[:viewport_y]).to eq(mouse_scroll_event.viewport_y)
    end
  end

  describe "POST #create" do
    it "creates a mouse scroll event" do
      session = create :session

      post :create,
           params: { mouse_scroll_event: { session_id: session.id,
                                           viewport_x: 1,
                                           viewport_y: 2,
                                           created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(json[:viewport_x]).to eq(1)
      expect(json[:viewport_y]).to eq(2)
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
