require 'rails_helper'

RSpec.describe Api::SessionsController, type: :controller do
  describe "GET #index" do
    it "returns all sessions" do
      create_list :session, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "returns detail for one session" do
      session = create :session

      get :show, params: { id: session.id }

      expect(json[:id]).to eq(session.id)
      expect(json[:pull_request][:id]).to eq(session.pull_request_id)
      expect(json[:user][:id]).to eq(session.user_id)
    end
  end

  describe "POST #create" do
    it "creates a session" do
      pull_request = create :pull_request
      user = create :user

      post :create,
           params: { session: { pull_request_id: pull_request.id,
                                user_id: user.id } }

      expect(json).to include(:id)
      expect(json[:pull_request][:id]).to eq(pull_request.id)
      expect(json[:user][:id]).to eq(user.id)
    end
  end
end
