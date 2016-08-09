require 'rails_helper'

RSpec.describe Api::MousePositionEventsController, type: :controller do
  describe "GET #index" do
    it "returns all mouse position events" do
      create_list :mouse_position_event, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one mouse position event" do
      mouse_position_event = create :mouse_position_event

      get :show, params: { id: mouse_position_event.id }

      expect(json[:id]).to eq(mouse_position_event.id)
      expect(json[:session][:id]).to eq(mouse_position_event.session_id)
      expect(json[:position_x]).to eq(mouse_position_event.position_x)
      expect(json[:position_y]).to eq(mouse_position_event.position_y)
      expect(json[:viewport_x]).to eq(mouse_position_event.viewport_x)
      expect(json[:viewport_y]).to eq(mouse_position_event.viewport_y)
    end
  end

  describe "POST #create" do
    it "creates a mouse position event" do
      session = create :session

      post :create,
           params: { mouse_position_event: { session_id: session.id,
                                             position_x: 1,
                                             position_y: 2,
                                             viewport_x: 3,
                                             viewport_y: 4,
                                             created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(json[:position_x]).to eq(1)
      expect(json[:position_y]).to eq(2)
      expect(json[:viewport_x]).to eq(3)
      expect(json[:viewport_y]).to eq(4)
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
