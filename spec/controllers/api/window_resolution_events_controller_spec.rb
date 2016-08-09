require 'rails_helper'

RSpec.describe Api::WindowResolutionEventsController, type: :controller do
  describe "GET #index" do
    it "returns all window resolution events" do
      create_list :window_resolution_event, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one window resolution event" do
      window_resolution_event = create :window_resolution_event

      get :show, params: { id: window_resolution_event.id }

      expect(json[:id]).to eq(window_resolution_event.id)
      expect(json[:session][:id]).to eq(window_resolution_event.session_id)
      expect(json[:width]).to eq(window_resolution_event.width)
      expect(json[:height]).to eq(window_resolution_event.height)
    end
  end

  describe "POST #create" do
    it "creates a window resolution event" do
      session = create :session

      post :create,
           params: { window_resolution_event: { session_id: session.id,
                                                width: 1,
                                                height: 2,
                                                created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(json[:width]).to eq(1)
      expect(json[:height]).to eq(2)
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
