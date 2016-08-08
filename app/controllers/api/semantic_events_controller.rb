class Api::SemanticEventsController < ApplicationController
  before_action :set_semantic_event, only: :show
  before_action :format_time, only: :create

  def index
    @semantic_events = SemanticEvent.all

    render json: @semantic_events
  end

  def show
    render json: @semantic_event
  end

  def create
    @semantic_event = SemanticEvent.new(semantic_event_params)

    if @semantic_event.save
      render json: @semantic_event, status: :created
    else
      render json: @semantic_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_semantic_event
    @semantic_event = SemanticEvent.find(params[:id])
  end

  def semantic_event_params
    params.require(:semantic_event).permit(:id, :session_id, :event_type_id, :element_type_id, :created_at)
  end

  def format_time
    begin
      params[:semantic_event][:created_at] = Time.parse(params[:semantic_event][:created_at]).utc.to_f
    rescue
      params[:semantic_event][:created_at] = Time.at(params[:semantic_event][:created_at].to_f).utc
    end
  end
end
