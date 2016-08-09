require 'rails_helper'

RSpec.describe Api::SemanticEventsController, type: :controller do
  describe "GET #index" do
    it "returns all semantic events" do
      create_list :semantic_event, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "shows detail for one semantic event" do
      semantic_event = create :semantic_event

      get :show, params: { id: semantic_event.id }

      expect(json[:id]).to eq(semantic_event.id)
      expect(json[:event_type][:id]).to eq(semantic_event.event_type_id)
      expect(json[:element_type][:id]).to eq(semantic_event.element_type_id)
    end
  end

  describe "POST #create" do
    it "creates a semantic event" do
      session = create :session
      event_type = create :event_type
      element_type = create :element_type

      post :create,
           params: { semantic_event: { session_id: session.id,
                                       event_type_id: event_type.id,
                                       element_type_id: element_type.id,
                                       created_at: 1.234 } }

      expect(json).to include(:id)
      expect(json[:session][:id]).to eq(session.id)
      expect(json[:event_type][:id]).to eq(event_type.id)
      expect(json[:element_type][:id]).to eq(element_type.id)
      expect(Time.parse(json[:created_at]).to_f).to be_within(0.001).of(1.234)
    end
  end
end
